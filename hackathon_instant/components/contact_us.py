import reflex as rx

def contact_us() -> rx.Component:
    return rx.flex(
        rx.box(class_name="w-[400px] border-t-2 border-[#1F1300] bg-[#001B2E] my-10"),
        rx.flex(
            rx.flex(
                rx.flex(
                    rx.text("Contact Us",size="9",class_name="font-semibold"),
                    rx.text("Fill out the form below. Someone from our side will reach out to you shortly.",size="4",direction="column"),
                    rx.input(placeholder="Name",size="3"),
                    rx.input(placeholder="Email",size="3"),
                    rx.flex(
                        rx.button("Submit",size="4",class_name="w-full", color_scheme="ruby"),class_name="pt-12 w-full"),   
                    direction="column",class_name="gap-6 max-w-[480px]"),
                rx.box(
                    rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"},width="380px",height="460px"),
                    ),
                    direction="row-reverse",
                    justify="between",
                    class_name={"gap-28 items-center w-full"}
                ),
                direction="column",
                class_name="gap-28"),
            direction="column",
            justify="between",
            class_name="gap-20 px-12 items-center"
            )