from .models.user import login, signup
from hackathon_instant.pages import *
import reflex as rx
from .models.store_data import fetch_all_products, install_shopify_app, publish_page, shopify_callback

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""
    

# Create the app.
app = rx.App()
app.api.add_api_route("/install-app/{shop_name}", install_shopify_app)
app.api.add_api_route("/auth/shopify/callback", shopify_callback)
app.api.add_api_route("/fetch-products/{store_name}", fetch_all_products)
app.api.add_api_route("/publish-page/{store_name}", publish_page)
app.api.add_api_route("/signup", signup, methods=["POST"])
app.api.add_api_route("/login", login, methods=["POST"])
