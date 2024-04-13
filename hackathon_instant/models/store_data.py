import binascii
from http.client import HTTPException
import os
import uuid
from fastapi.responses import RedirectResponse
import requests
import shopify
import urllib.parse

from sqlalchemy import Column, DateTime
from datetime import datetime
from sqlmodel import Field
import reflex as rx

class StoreData(rx.Model, table=True):
     id: str = Field(primary_key = True, nullable = False, unique = True, default=uuid.uuid4())
     store_name: str = Field(nullable=False, unique = True)
     access_token: str = Field(nullable=True)    
     is_app_install: bool = Field(nullable=False, default=False)
     created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
     updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

shopify_api_key = "7a84338d7b85067ec1f557c70313ff47"
shopify_api_secret = "1a9e0c7a634380de0b56bb6ec7119cb0"

async def install_shopify_app(shop_name: str):
    if not shop_name:
        raise HTTPException(status_code=400, detail="Shop parameter is missing")
    
    stores = await find_one_store(shop_name)
    
    if not stores:
        await create_store(shop_name, is_app_install=False, access_token=None)
        
    if stores and stores.is_app_install:
        raise HTTPException(status_code=400, detail="App already installed for this store")
    
    shopify.Session.setup(api_key=shopify_api_key, secret=shopify_api_secret)    
    shop_url = "quickstart-4cb07f3a.myshopify.com"
    api_version = '2024-01'
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    redirect_uri = "https://6d64-112-196-47-10.ngrok-free.app/auth/shopify/callback"
    scopes = ['read_products', 'read_orders']

    newSession = shopify.Session(shop_url, api_version)
    auth_url = newSession.create_permission_url(scopes, redirect_uri, state)
        
    return RedirectResponse(auth_url)


async def shopify_callback(code: str | None = None, shop: str | None = None, state: str | None = None, hmac: str | None = None, host: str | None = None, timestamp: int | None = None):
    if not code or not shop or not state:
        raise HTTPException(status_code=400, detail="Missing code, shop, or state parameter")
    
    accessTokenUrl = f"https://{shop}/admin/oauth/access_token"
    accessParams = {
        "client_id": shopify_api_key,
        "client_secret": shopify_api_secret,
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
    
    return {"message": "Shopify Auth Callback"}

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