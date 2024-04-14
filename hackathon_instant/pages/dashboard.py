"""The dashboard page."""

import requests.cookies
from hackathon_instant.templates import template
import reflex as rx
import requests
import http.cookies
from fastapi import Cookie
from ..components.template import template as template_to_render

from hackathon_instant.components.landingPage.header import header
from hackathon_instant.components.landingPage.hero_section import hero_section
from hackathon_instant.components.landingPage.benefits import benefits
from hackathon_instant.components.landingPage.team import team
from hackathon_instant.components.landingPage.functions import functions
from hackathon_instant.components.landingPage.start import start
from hackathon_instant.components.landingPage.footer import footer
from ..models.user import signup as register
from ..models.user import login as login_user
from ..models.user import store_list 
from ..models.store_data import install_shopify_app as connect
from ..cookie import CookieState
from ..models.cookie import get_cookie_from_header

import reflex as rx

class Stores(rx.State):

    mycookie=""
    stores=[]
    is_loading = False

    async def fetch_store(self):
        mycookie = await self.get_state(CookieState)
        stores = await store_list(mycookie.custom_cookie[0])
        self.is_loading = True
        self.stores=stores


class SectionPanelState(rx.State):
    section: str = ''
    sectionList: list = []

    def set_section(self, selectedSection):
        self.section = selectedSection
        self.add_in_list(selectedSection)  # Adding directly when section is set.

    def add_in_list(self, selectedSection):
        if selectedSection not in self.sectionList:  # Check to avoid duplicates.
            self.sectionList.append(selectedSection)

    def filter_list(self, filter_term: str):
        self.sectionList = [item for item in self.sectionList if filter_term not in item]
        self.section = ''
        
def list_item(section: str):
        return rx.box(rx.text(section))


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:

    return rx.hstack(
        rx.box(
       rx.vstack(
                rx.heading("Sections", size="5", class_name="py-2"),
                rx.flex(
                        rx.card("Header", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Header'),),
                        rx.card("Carousel", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Carousel')),
                        rx.card("Featured Product", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Featured Product')),
                        rx.card("Contact Us", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Contact Us')),
                        rx.card("Footer", class_name="cursor-pointer transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Footer')),
                        spacing="2",
                        width="100%",
                        direction="column"
                ),
                rx.text(SectionPanelState.section),
                rx.button("Remove Section", on_click=lambda: SectionPanelState.filter_list(SectionPanelState.section)),
                class_name="border-l h-screen p-4 w-[300px]"
                ),
                class_name="fixed right-0 top-0",
    ),
    rx.vstack(
        rx.foreach(SectionPanelState.sectionList, list_item),
    )
    )


class FormInputState(rx.State):
    form_data: dict = {
        "name":"",
        "username":"",
        "password":"",
        "shopify_url":""
    }
    async def handle_signup(self, form_data: dict):
        self.form_data = form_data
        print("form_data",form_data)
        response =await register(form_data["name"],form_data["username"],form_data["password"])
        print(response)
        if(response["status_code"]):
            yield[CookieState.set_custom_cookie(response["access_token"]),rx.redirect("/shopify-connect")]
        else:
            print("error")
            return
            

    async def handle_login(self, form_data: dict):
        self.form_data = form_data
        response =await login_user(form_data["username"],form_data["password"])
        print(response)
        if(response["status_code"]):
            yield[CookieState.set_custom_cookie(response["access_token"]),rx.redirect("/shopify-connect")]
        else:
            print("error")
            return
        
    async def handle_store_connect(self, form_data: dict):
        self.form_data = form_data
        mycookie = await self.get_state(CookieState)
        print("<><><><><><",mycookie.custom_cookie[0])
        auth_url =await connect(form_data["shopify_url"],mycookie.custom_cookie[0])
        print(auth_url)
        if(auth_url):
            return rx.redirect(auth_url)
        else:
            print("error")
            return

@rx.page("/login")
def login() -> rx.Component:

    return rx.flex(
        rx.text("Hi there, Welcome back", size="7", class_name="font-semibold"),
        rx.form.root(
        rx.flex(
            rx.input(name="username",required=True, placeholder="Username", size="3", width="400px", height="50px", variant="soft", color_scheme="violet"),
            rx.input(name="password",required=True, placeholder="Password",type="password", size="3", width="400px", height="50px", variant="soft", color_scheme="violet"),
            direction="column",
            class_name="gap-6 pb-8"
        ),
        rx.button("Login",type="submit", size="4", color_scheme="violet", class_name="max-w-[400px] w-full"),on_submit=FormInputState.handle_login,
            reset_on_submit=True,class_name="max-w-[400px] w-full"),
        direction="column",
        justify="center",
        class_name="w-screen h-screen gap-10 items-center"
    )


@rx.page("/signup")
def signup() -> rx.Component:
    return rx.flex(
        rx.text("Getting Started", size="7", class_name="font-semibold"),
        rx.form.root(
        rx.flex(
            rx.input(name="name",required=True, placeholder="Name",size="3",width="400px",height="50px",variant="soft",color_scheme="violet"),
            rx.input(name="username",required=True, placeholder="Username", size="3", width="400px", height="50px", variant="soft", color_scheme="violet"),
            rx.input(name="password",placeholder="Password",type="password",required=True, size="3", width="400px", height="50px", variant="soft", color_scheme="violet"),
            direction="column",
            class_name="gap-6 pb-8"
        ),
        rx.button("Sign Up",type="submit", size="4", color_scheme="violet", class_name="max-w-[400px] w-full"),on_submit=FormInputState.handle_signup,
            reset_on_submit=True,class_name="max-w-[400px] w-full"),
        direction="column",
        justify="center",
        class_name="w-screen h-screen gap-10 items-center"
    )

@rx.page("/template")
def template()-> rx.Component:
    return template_to_render()

@rx.page("/")
def landing_page() -> rx.Component:

   return rx.flex(
                rx.flex(
                    header(),
                hero_section(),
                class_name="h-[95vh] flex flex-col"),
                benefits(),
                team(),
               functions(),
              start(),
              footer(),
        class_name="flex flex-col font-mono")

@rx.page("/shopify-connect")
def shopify_connect()-> rx.Component:
    return rx.flex(
        rx.text("Hi there, Welcome back", size="7", class_name="font-semibold"),
        rx.form.root(
        rx.flex(
            rx.input(name="shopify_url",required=True, placeholder="Enter you Shopify URL", size="3", width="400px", height="50px", variant="soft", color_scheme="violet"),
            direction="column",
            class_name="gap-6 pb-8"
        ),
        rx.button("Connect",type="submit", size="4", color_scheme="violet", class_name="max-w-[400px] w-full"),on_submit=FormInputState.handle_store_connect,
            reset_on_submit=True,class_name="max-w-[400px] w-full"),
        direction="column",
        justify="center",
        class_name="w-screen h-screen gap-10 items-center"
    )


app = rx.App()
app.api.add_api_route("/signup", register, methods=["POST"])
app.api.add_api_route("/login", login_user, methods=["POST"])
app.api.add_api_route("/shopify-connect", connect, methods=["POST"])
app.api.add_api_route("/shopify-connect", get_cookie_from_header, methods=["POST"])
app.api.add_api_route("/shopify-connect", store_list, methods=["GET"])
