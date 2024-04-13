import binascii
from http.client import HTTPException
import os
from fastapi.responses import RedirectResponse
import requests
import shopify
import urllib.parse

session_repository = dict()

shop_name = "hackathon-instant"
shopify_api_key = "7a84338d7b85067ec1f557c70313ff47"
shopify_api_secret = "1a9e0c7a634380de0b56bb6ec7119cb0"

def install_shopify_app(shop_name: str):
    if not shop_name:
        raise HTTPException(status_code=400, detail="Shop parameter is missing")
    
    print(shopify_api_key, shopify_api_secret)
    
    shopify.Session.setup(api_key=shopify_api_key, secret=shopify_api_secret)    
    shop_url = "quickstart-4cb07f3a.myshopify.com"
    api_version = '2024-01'
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    redirect_uri = "https://2546-112-196-47-10.ngrok-free.app/auth/shopify/callback"
    scopes = ['read_products', 'read_orders']

    newSession = shopify.Session(shop_url, api_version)
    auth_url = newSession.create_permission_url(scopes, redirect_uri, state)
    print(auth_url)
        
    return RedirectResponse(auth_url)


def shopify_callback(code: str | None = None, shop: str | None = None, state: str | None = None, hmac: str | None = None, host: str | None = None, timestamp: int | None = None):
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
    print("Access Token:", access_token)
    return {"message": "Shopify Auth Callback"}

async def find_one_store(store_name: str):
    # Logic to find store data from the database
    pass

    