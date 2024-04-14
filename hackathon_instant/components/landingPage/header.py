import reflex as rx

from hackathon_instant.cookie import CookieState
from hackathon_instant.models.user import store_list


def header() -> rx.Component:

      return rx.flex(
        rx.flex(
             rx.image(src="logo.png", width="50px", height="50px"),
             rx.text("Craftify", class_name="text-2xl font-semibold hidden md:block text-[#4F2956]"),
             spacing="3",
             class_name="items-center flex"
        ),
        rx.button("Login", color_scheme="violet",width="100px",size="3",on_click=rx.redirect("/login")),
        justify="between",
        class_name="px-2 md:px-[80px] py-4 bg-[#EAE3F8] flex items-center"
        )