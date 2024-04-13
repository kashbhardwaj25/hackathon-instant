"""The dashboard page."""

from hackathon_instant.templates import template
from hackathon_instant.components.sidebar import sidebar
from hackathon_instant.components.sectionpanel import sectionpanel

import reflex as rx

@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.box(
       sectionpanel(),
       class_name="fixed right-0 top-0"
    )
