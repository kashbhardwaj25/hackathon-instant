import reflex as rx

def footer() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text("All rights Reserved. © 2021"),rx.text("Privacy Policy"),rx.text("Terms of Service"),rx.text("Contact Us"),
            direction="row",justify="between",class_name={"md:text-left text-center w-full"}),
    direction="row",
    justify="between",
    class_name={"px-8 md:px-16 py-8 border-[#1F1300] items-center w-full bg-[#001B2E] mt-32 text-[#F0E7D8]"}
    )