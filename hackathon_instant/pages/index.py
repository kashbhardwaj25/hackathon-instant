"""The home page of the app."""

from hackathon_instant import styles
from hackathon_instant.templates import template

import reflex as rx

def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()

    return rx.text("hi")