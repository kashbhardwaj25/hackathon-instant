import reflex as rx
from hackathon_instant.templates import template

class State(rx.State):
    """The app state."""


def card()-> rx.Component:
    return rx.container(rx.container(rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"}, width="700px",class_name={"p-3"}, height="auto"),rx.text("Mens Printed Casual Shirt",size="3",align="center",class_name="text-white"),
                         rx.flex(
                             rx.text("S",class_name="text-white opacity-40 hover:opacity-100"),
                             rx.text("M",class_name="text-white opacity-40 hover:opacity-100"),
                             rx.text("L",class_name="text-white opacity-40 hover:opacity-100"),
                             rx.text("XL",class_name="text-white opacity-40 hover:opacity-100"),justify="center",class_name="gap-6 text-sm"),class_name={"bg-slate-800 cursor-pointer max-w-[250px] rounded-xl w-full h-[380px] relative"}),class_name="relative")

@template(route="/template", title="Template1")
def index() -> rx.Component:
    return rx.flex(
    rx.flex(
        rx.text("Logo"),
        rx.flex(
            rx.text("Products"),rx.text("Testimonials"),rx.text("Contact"),rx.text("Buy Now"),
            direction="row",justify="between",class_name={"gap-16"}),
    direction="row",
    justify="between",
    class_name={"px-16 py-8"}
    ),
    rx.flex(
        rx.flex(
            rx.text(
                "A field guide to the world of modern web development",size="9",class_name={"font-bold max-w-[800px] text-center"}),
                justify="center",class_name={"w-full"}
                ),
            ),
    rx.flex(
        rx.button("Buy Now",size="4"),
        rx.button("Read More",size="4"),
        direction="row",
        justify="center",
        class_name={"w-full gap-8"}
        ),
    
    rx.flex(
        rx.text("Carousel",align="center",size="5",class_name={"text-white"}),
        rx.flex(
            card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),
            class_name={"w-full gap-8 overflow-x-scroll py-10"},
        ),
        direction="column",
    ),
    direction="column",
    justify="center",
    class_name={"px-16 py-8 w-full bg-slate-500 gap-10"},
    )
    


app = rx.App()
app.add_page(index)
