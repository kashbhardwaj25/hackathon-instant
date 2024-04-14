import reflex as rx

def header() -> rx.Component:
    return rx.flex(
        rx.avatar(variant="solid", color_scheme="ruby"),
        rx.flex(
            rx.text("Products"),rx.text("Testimonials"),rx.text("Contact"),rx.text("Buy Now"),
            direction="row",justify="between",class_name={"gap-16"}),
    direction="row",
    justify="between",
    class_name={"px-16 py-8 border-[#1F1300] items-center w-full bg-[#001B2E] text-[#F0E7D8]"}
    )