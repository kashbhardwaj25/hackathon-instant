from datetime import datetime
from sqlmodel import Field
from hackathon_instant.pages import *

import reflex as rx

from sqlalchemy import Column, DateTime

from .shopify_service import install_shopify_app, shopify_callback

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""
    

class StoreData(rx.Model, table=True):
     id: str = Field(primary_key = True, nullable = False, unique = True,)
     store_name: str = Field(nullable=False, unique = True)
     access_token: str = Field(nullable=True)    
     is_app_install: bool = Field(nullable=False, default=False)
     created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
     updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

# Create the app.
app = rx.App()
app.api.add_api_route("/install-app/{shop_name}", install_shopify_app)
app.api.add_api_route("/auth/shopify/callback", shopify_callback)
