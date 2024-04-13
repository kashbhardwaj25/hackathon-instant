from hackathon_instant.pages import *
import reflex as rx
from .models.store_data import install_shopify_app, shopify_callback

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""
    

# Create the app.
app = rx.App()
app.api.add_api_route("/install-app/{shop_name}", install_shopify_app)
app.api.add_api_route("/auth/shopify/callback", shopify_callback)
