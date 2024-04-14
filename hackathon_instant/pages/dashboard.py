"""The dashboard page."""

from hackathon_instant.templates import template
import reflex as rx
import requests
import http.cookies
from ..components.template import template as template_to_render

import reflex as rx

class SectionPanelState(rx.State):
    section: str = ''

    def set_section(self, selectedSection):
        self.section = selectedSection


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.box(
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
                rx.button("Add Section"),
                class_name="border-l h-screen p-4 w-[300px]"
                ),
                class_name="fixed right-0 top-0"
    )


class FormInputState(rx.State):
    form_data: dict = {
        "username":"",
        "name":"",
        "password":""
    }
    def handle_signup(self, form_data: dict):
        self.form_data = form_data
        make_signup_api_call(form_data["username"], form_data["name"] ,form_data["password"])

    def handle_login(self, form_data: dict):
        self.form_data = form_data
        make_login_api_call(self.form_data["username"], self.form_data["password"])


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


def make_login_api_call(username: str, password: str):
    url = "https://example.com/api/login"  # Adjusted to point to a signup endpoint
    data = {'username': username,'password': password}
    print("API call with:", username, password)

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Login successful")
            # Assuming the token is returned in the response JSON under the key 'token'
            token = response.json().get('token')
            if token:
                add_token_to_cookies(token)
        else:
            print("Login failed with status code:", response.status_code)
    except requests.RequestException as e:
        print("An error occurred:", e)

@rx.page("/signup")
def signup() -> rx.Component:
    return rx.flex(
        rx.text("Getting Started", size="7", class_name="font-semibold"),
        rx.form.root(
        rx.flex(
            rx.input(name="name",required=True, placeholder="Name",size="3",width="400px",height="50px",variant="soft",color_scheme="violet"),
            rx.input(name="username",required=True, placeholder="username", size="3", width="400px", height="50px", variant="soft", color_scheme="violet"),
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


def make_signup_api_call(username: str,name:str, password: str):
    url = "https://example.com/api/signup"  # Adjusted to point to a signup endpoint
    data = {'username': username, 'name': name, 'password': password}
    print("API call with:", username, name, password)

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Signup successful")
            # Assuming the token is returned in the response JSON under the key 'token'
            token = response.json().get('token')
            if token:
                add_token_to_cookies(token)
        else:
            print("Signup failed with status code:", response.status_code)
    except requests.RequestException as e:
        print("An error occurred:", e)

def add_token_to_cookies(token):
    cookie = http.cookies.SimpleCookie()
    cookie["auth_token"] = token
    cookie["auth_token"]["path"] = "/"
    cookie["auth_token"]["httponly"] = True
    print("Cookie set:", cookie.output())

@rx.page("/template")
def template()-> rx.Component:
    return template_to_render()
