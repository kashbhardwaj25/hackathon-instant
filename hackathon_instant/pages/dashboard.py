"""The dashboard page."""

from hackathon_instant.templates import template
import reflex as rx
import requests
import http.cookies
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
from ..cookie import CookieState


import reflex as rx

carousel="""
<div style="overflow-x: auto; white-space: nowrap; padding: 20px; background-color: #f4f4f4; width: 1000px;">\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 1</h3>\n
        <p style="color: #555; font-size: 14px;">Name</p>\n
    </div>\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 2</h3>\n
        <p style="color: #555; font-size: 14px;">Name.</p>\n
    </div>\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 3</h3>\n
        <p style="color: #555; font-size: 14px;">Name</p>\n
    </div>\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 4</h3>\n
        <p style="color: #555; font-size: 14px;">Name</p>\n
    </div>\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 5</h3>\n
        <p style="color: #555; font-size: 14px;">Name</p>\n
    </div>\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 6</h3>\n
        <p style="color: #555; font-size: 14px;">Name</p>\n
    </div>\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 7</h3>\n
        <p style="color: #555; font-size: 14px;">Name</p>\n
    </div>\n
    <div style="display: inline-block; width: 200px; margin-right: 20px; background-color: white; text-align: center; padding: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">\n
        <img src="https://images.pexels.com/photos/8947774/pexels-photo-8947774.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" style="width: 100%; border-radius: 5px;">\n
        <h3 style="color: #333;">Product 8</h3>\n
        <p style="color: #555; font-size: 14px;">Name</p>\n
    </div>\n
</div>\n
"""

navbar_html = """
<div style="width: 1000px; background-color: #333; overflow: hidden; display: flex; justify-content: space-between; align-items: center; padding: 10px 20px;">\n
  <div style="float: left; color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px;">\n
    <b>SiteName</b>\n
  </div>\n
  <div style="display: flex; float: right;">\n
    <a href="#home" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">Home</a>\n
    <a href="#services" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">Services</a>\n
    <a href="#about" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">About</a>\n
    <a href="#contact" style="color: white; text-align: center; padding: 14px 16px; text-decoration: none; font-size: 17px; display: block;">Contact</a>\n
  </div>\n
</div>\n
"""

hero_html = """
<div class="hero" style="width: 1000px; background-image: url('https://images.pexels.com/photos/2563597/pexels-photo-2563597.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'); height: 100vh; background-size: cover; background-position: center; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; color: white;">\n
  <h1>Welcome to Our World</h1>\n
  <p>Explore the beauty of nature with us.</p>\n
  <a href="#more" class="cta-button" style="padding: 12px 25px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">Discover More</a>\n
</div>\n
"""

contact_us_html = """
<div style="display: flex; align-items: center; justify-content: center; padding: 20px; width: 1000px;">\n
  <div style="flex: 1; min-height: 300px; background-image: url('https://images.pexels.com/photos/2563597/pexels-photo-2563597.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'); background-size: cover; background-position: center;"></div>\n
  <div style="flex: 1; padding: 20px;">\n
    <form action="submit-your-form-handler" method="POST" style="display: flex; flex-direction: column; gap: 10px;">\n
      <label for="name" style="color: #333; font-weight: bold;">Name:</label>\n
      <input type="text" id="name" name="name" style="padding: 8px; border-radius: 4px; border: 1px solid #ccc;">\n

      <label for="email" style="color: #333; font-weight: bold;">Email:</label>\n
      <input type="email" id="email" name="email" style="padding: 8px; border-radius: 4px; border: 1px solid #ccc;">\n

      <label for="message" style="color: #333; font-weight: bold;">Message:</label>\n
      <textarea id="message" name="message" rows="4" style="padding: 8px; border-radius: 4px; border: 1px solid #ccc;"></textarea>\n

      <button type="submit" style="background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send</button>\n
    </form>\n
  </div>\n
</div>\n
"""

class SectionPanelState(rx.State):
    section: str = ''
    sectionList: list = []
    finalHtml: str = ''

    def set_section(self, selectedSection):
        self.section = selectedSection
        self.add_in_list(selectedSection)  # Adding directly when section is set.

    def add_in_list(self, selectedSection):
        if selectedSection not in self.sectionList:  # Check to avoid duplicates.
            self.sectionList.append(selectedSection)

    def filter_list(self, filter_term: str):
        self.sectionList = [item for item in self.sectionList if filter_term not in item]
        self.section = ''
        
    def finalise_html(self):
        for section in self.sectionList:
            if section == "Header":
                self.finalHtml == self.finalHtml + navbar_html
            elif section == "Carousel":
                self.finalHtml == self.finalHtml + carousel
            elif section == "Hero Section":
                self.finalHtml == self.finalHtml + hero_html
            elif section == "Contact Us":
                self.finalHtml = self.finalHtml + contact_us_html
            else:
                self.finalHtml = self.finalHtml + ""
                
def list_item(section: str):
   return rx.match(
        section,
        ("Header", rx.html(navbar_html)),
        ("Carousel", rx.html(carousel)),
        ("Hero Section", rx.html(hero_html)),
        ("Contact Us", rx.html(contact_us_html)),
        ("", rx.text("Section not found")),
    )


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.hstack(
        rx.box(
       rx.vstack(
                rx.heading("Sections", size="5", class_name="py-2"),
                rx.flex(
                        rx.card("Header", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Header'),),
                        rx.card("Carousel", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Carousel')),
                        rx.card("Hero Section", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Hero Section')),
                        rx.card("Contact Us", class_name="cursor-pointer hover:transition-all hover:bg-rose-50", on_click=lambda: SectionPanelState.set_section('Contact Us')),
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
        class_name="w-[90vh]"
    )
    )


class FormInputState(rx.State):
    form_data: dict = {
        "name":"",
        "username":"",
        "password":""
    }
    async def handle_signup(self, form_data: dict):
        self.form_data = form_data
        print("form_data",form_data)
        response =await register(form_data["name"],form_data["username"],form_data["password"])
        print(response)
        if(response["status_code"]):
            yield[CookieState.set_custom_cookie(response["access_token"]),rx.redirect("/dashboard")]
        else:
            print("error")
            return
            

    async def handle_login(self, form_data: dict):
        self.form_data = form_data
        response =await login_user(form_data["username"],form_data["password"])
        print(response)
        if(response["status_code"]):
            yield[CookieState.set_custom_cookie(response["access_token"]),rx.redirect("/dashboard")]
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

app = rx.App()
app.api.add_api_route("/signup", register, methods=["POST"])
app.api.add_api_route("/login", login_user, methods=["POST"])