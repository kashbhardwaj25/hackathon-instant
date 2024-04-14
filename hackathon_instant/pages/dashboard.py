"""The dashboard page."""

from hackathon_instant.templates import template

import reflex as rx

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
