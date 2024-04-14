import reflex as rx

def hero_section() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.flex(
                rx.text(
                    "A field guide to the world of modern web development",size="9",class_name={"font-bold max-w-[800px] text-center"}),
                    justify="center",class_name={"w-full py-8"}
                    ),
                    class_name="mt-20"
                ),
            rx.flex(
                rx.button("Buy Now",size="4",color_scheme="ruby"),
                rx.button("Read More",size="4",color_scheme="ruby"),
                direction="row",
                justify="center",
                class_name={"w-full gap-4 items-center"}
                ),
                direction="column")