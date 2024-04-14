import binascii
from http.client import HTTPException
import os
import uuid
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import requests
import shopify
import urllib.parse

from sqlalchemy import Column, DateTime
from datetime import datetime
from sqlmodel import Field
import reflex as rx

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Constants
SHOPIFY_API_KEY = os.getenv('SHOPIFY_API_KEY')
SHOPIFY_API_SECRET = os.getenv('SHOPIFY_API_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
FE_URL = os.getenv('FE_URL')

class PageData(BaseModel):
    shop_name: str
    title: str
    body_html: str
    page_id: int = None

class StoreData(rx.Model, table=True):
     id: str = Field(primary_key = True, nullable = False, unique = True, default=uuid.uuid4())
     store_name: str = Field(nullable=False, unique = True)
     access_token: str = Field(nullable=True)    
     is_app_install: bool = Field(nullable=False, default=False)
     created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
     updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

async def install_shopify_app(shop_name: str):
    if not shop_name:
        raise HTTPException(status_code=400, detail="Shop parameter is missing")
    
    stores = await find_one_store(shop_name)
    
    if not stores:
        await create_store(shop_name, is_app_install=False, access_token=None)
        
    if stores and stores.is_app_install:
        raise HTTPException(status_code=400, detail="App already installed for this store")
    
    shopify.Session.setup(api_key=SHOPIFY_API_KEY, secret=SHOPIFY_API_SECRET)    
    shop_url = f"{shop_name}.myshopify.com"
    api_version = '2024-01'
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    redirect_uri = REDIRECT_URI
    scopes = ['read_products', 'write_products', 'read_orders', 'write_content', 'read_content']

    newSession = shopify.Session(shop_url, api_version)
    auth_url = newSession.create_permission_url(scopes, redirect_uri, state)
        
    return RedirectResponse(auth_url)


async def shopify_callback(code: str | None = None, shop: str | None = None, state: str | None = None, hmac: str | None = None, host: str | None = None, timestamp: int | None = None):
    if not code or not shop or not state:
        raise HTTPException(status_code=400, detail="Missing code, shop, or state parameter")
    
    accessTokenUrl = f"https://{shop}/admin/oauth/access_token"
    accessParams = {
        "client_id": SHOPIFY_API_KEY,
        "client_secret": SHOPIFY_API_SECRET,
        "code": code,
    }

    response = requests.post(accessTokenUrl, params=urllib.parse.urlencode(accessParams))
    data = response.json()

    access_token = data["access_token"]
    store_name = shop.split(".")[0]
    
    stores = await find_one_store(store_name)
    
    if not stores:
        raise HTTPException(status_code=400, detail="Store not found")
    
    await update_store(store_name, is_app_install=True, access_token=access_token)
    
    return RedirectResponse(FE_URL)

async def fetch_all_products(store_name):
    store_data = await find_one_store(store_name)

    if not store_data or store_data.is_app_install == False:
        return "Store not found or app not installed"

    access_token = store_data.access_token
    shopify_api_url = f"https://{store_name}.myshopify.com/admin/api/2024-01/products.json"

    # Use requests to fetch products from Shopify
    headers = {
        "X-Shopify-Access-Token": access_token,
    }

    response = requests.get(shopify_api_url, headers=headers)
    products = response.json()['products']

    return products


async def publish_page(store_name: str):
    # Retrieve store data from the database
    store_data = await find_one_store(store_name)
    
    if not store_data or not store_data.is_app_install:
        raise HTTPException(status_code=404, detail="Store not found or app not installed")

    # Setup Shopify session
    shopify.Session.setup(api_key=SHOPIFY_API_KEY, secret=SHOPIFY_API_SECRET)
    session = shopify.Session(f"{store_name}.myshopify.com", "2024-01", store_data.access_token)
    shopify.ShopifyResource.activate_session(session)

    # Create or update Shopify page
    # if page_data.page_id:
    #     page = shopify.Page.find(page_data.page_id)
    #     if not page:
    #         raise HTTPException(status_code=404, detail="Page not found")
    # else:
    #     page = shopify.Page()
        
    page = shopify.Page()

    page.title = "Amit Bishnoi Custom Page"
    page.body_html = "<h2>Bhaiyon Publish Hogya</h2>\n<p>Revert in Slack Group If you want to congratulate us <strong>Within 15 minutes and this is strong tag of html</strong>.</p>"
    page.handle = "amit-page"
    success = page.save() 

    shopify.ShopifyResource.clear_session()

    if success:
        page_url = f"https://{store_name}.myshopify.com/pages/{page.handle}"
        
        return RedirectResponse(page_url)
    else:
        raise HTTPException(status_code=500, detail="Failed to publish page")

async def find_one_store(store_name: str):
    with rx.session() as session:
        result = session.exec(StoreData.select().where(StoreData.store_name == store_name))
        store =  result.first()
        return store

async def create_store(store_name: str, access_token: str, is_app_install: bool):
    with rx.session() as session:
        store = StoreData(store_name=store_name, access_token=access_token, is_app_install=is_app_install)
        session.add(store)
        session.commit()
        
async def update_store(store_name: str, is_app_install: bool, access_token: str):
    with rx.session() as session:
        result = session.exec(StoreData.select().where(StoreData.store_name == store_name))
        store = result.first()
        store.is_app_install = is_app_install
        store.access_token = access_token
        session.commit()