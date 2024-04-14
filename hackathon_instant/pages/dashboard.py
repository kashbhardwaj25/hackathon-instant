"""The dashboard page."""

from hackathon_instant.templates import template

from hackathon_instant.components.landingPage.header import header
from hackathon_instant.components.landingPage.hero_section import hero_section
from hackathon_instant.components.landingPage.benefits import benefits
from hackathon_instant.components.landingPage.team import team
from hackathon_instant.components.landingPage.functions import functions
from hackathon_instant.components.landingPage.start import start
from hackathon_instant.components.landingPage.footer import footer

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
