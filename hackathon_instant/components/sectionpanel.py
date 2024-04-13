"""Sidebar component for the app."""

import reflex as rx

def sectionpanel() -> rx.Component:
    """The sectionpanel.

    Returns:
        The sectionpanel component.
    """
    # Get all the decorated pages and add them to the sidebar.
    return rx.vstack(
      rx.heading("Sections", size="5", class_name="py-2"),
      rx.flex(
              rx.card("Header", class_name="cursor-pointer hover:transition-all hover:bg-rose-50"),
              rx.card("Carousel", class_name="cursor-pointer hover:transition-all hover:bg-rose-50"),
              rx.card("Featured Product", class_name="cursor-pointer hover:transition-all hover:bg-rose-50"),
              rx.card("Contact Us", class_name="cursor-pointer hover:transition-all hover:bg-rose-50"),
              rx.card("Footer", class_name="cursor-pointer transition-all hover:bg-rose-50"),
              spacing="2",
              width="100%",
              direction="column"
    ),
    rx.box(
      rx.heading("Attributes", size="5", class_name="py-2"),
    ),
    class_name="border-l h-screen p-4 w-[300px]"
)
