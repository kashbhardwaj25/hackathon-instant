import reflex as rx

def feature_section() -> rx.Component:
    return rx.flex(
        rx.box(class_name="w-[400px] border-t-2 border-[#1F1300] my-4 bg-[#001B2E]"),
        rx.flex(
            rx.flex(
                rx.flex(
                    rx.text("Get all Essentials you are looking for in a light package",size="9"),
                    rx.text("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.",size="4",direction="column"),
                    rx.button("Discover More",size="4",color_scheme="ruby"),
                    direction="column",class_name="gap-8 max-w-[540px] text-center md:text-left"),
                rx.box(
                    rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"},width="380px",height="460px",class_name={"hidden md:flex"}),
                    class_name={"h-[430px]"}
                    ),
                    justify="between",
                    class_name={"md:gap-28 w-full items-center"}
                ),
                direction="column",
                class_name="gap-20"),
                rx.box(
                    rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"},width="380px",height="460px",class_name={"flex md:hidden"}),
                    class_name={"h-[430px]"}
                    ),
            direction="column",
            justify="between",
            class_name="gap-8 md:gap-20 py-12 px-16 items-center"
            )