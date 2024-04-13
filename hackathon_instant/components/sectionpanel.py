"""Sidebar component for the app."""

import reflex as rx

class SectionPanelState(rx.State):
    section: str = ''

    def set_section(self, selectedSection):
        self.section = selectedSection

def sectionpanel() -> rx.Component:
    """The sectionpanel.

    Returns:
        The sectionpanel component.
    """
    # Get all the decorated pages and add them to the sidebar.
    return rx.vstack(
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
    rx.box(
      rx.heading("Attributes", size="5", class_name="py-2"),
    ),
    rx.text(SectionPanelState.section),
    rx.button("Add Section"),
    class_name="border-l h-screen p-4 w-[300px]"
)
