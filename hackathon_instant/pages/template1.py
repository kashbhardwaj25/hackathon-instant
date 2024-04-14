import reflex as rx
class State(rx.State):
    """The app state."""


def card()-> rx.Component:
    return rx.container(rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"}, width="700px",class_name={"p-3"}, height="auto"),rx.text("Mens Printed Casual Shirt",size="3",align="center",class_name="text-white"),
                         rx.flex(
                             rx.text("S",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("M",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("L",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("XL",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),justify="center",class_name="gap-6 text-sm"),class_name={"bg-[#001B2E] drop-shadow-lg cursor-pointer max-w-[250px] rounded-xl w-full h-[380px]"})


def index() -> rx.Component:
    return rx.flex(
    rx.flex(
        rx.avatar(variant="solid", color_scheme="ruby"),
        rx.flex(
            rx.text("Products"),rx.text("Testimonials"),rx.text("Contact"),rx.text("Buy Now"),
            direction="row",justify="between",class_name={"gap-16"}),
    direction="row",
    justify="between",
    class_name={"px-16 py-8 border-[#1F1300] items-center w-full bg-[#001B2E] text-[#F0E7D8]"}
    ),
    rx.flex(
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

     rx.flex(
        rx.box(class_name="w-[400px] border-t-2 border-[#1F1300] my-4 bg-[#001B2E]"),
        rx.flex(
            rx.flex(
                rx.flex(
                    rx.text("Get all Essentials you are looking for in a light package",size="9"),
                    rx.text("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.",size="4",direction="column"),
                    rx.button("Discover More",size="4",color_scheme="ruby"),
                    direction="column",class_name="gap-8 max-w-[540px]"),
                rx.box(
                    rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"},width="380px",height="460px"),
                    class_name={"h-[430px]"}
                    ),
                    justify="between",
                    class_name={"gap-28 w-full items-center"}
                ),
                direction="column",
                class_name="gap-20"),
            direction="column",
            justify="between",
            class_name="gap-20 py-12 px-16 items-center"
            ),
    rx.flex(
        rx.box(class_name="w-[400px] border-t-2 border-[#1F1300] my-12 bg-[#001B2E]"),
        rx.text("Feel free to explore our Products",align="center",size="7",class_name={"font-semibold pb-4 text-[#1F1300]"}),
        rx.flex(
            card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),
            class_name={"w-full gap-8 overflow-x-scroll py-10"},
        ),
        direction="column",justify="center",class_name="items-center",
    ),
    rx.flex(
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
            ),
        direction="column",
        justify="center",
        class_name={"px-32 py-8 w-full bg-[#F0E7D8] gap-10 text-[#1F1300]"}),
    direction="column",
    )
    


app = rx.App()
app.add_page(index)
