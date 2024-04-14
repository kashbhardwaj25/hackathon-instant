import reflex as rx

def card()-> rx.Component:
    return rx.container(rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"}, width="700px",class_name={"p-3"}, height="auto"),rx.text("Mens Printed Casual Shirt",size="3",align="center",class_name="text-white"),
                         rx.flex(
                             rx.text("S",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("M",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("L",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("XL",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),justify="center",class_name="gap-6 text-sm"),class_name={"bg-[#001B2E] drop-shadow-lg cursor-pointer max-w-[250px] rounded-xl w-full h-[380px]"})

def crousel() -> rx.Component:
    return rx.flex(
        rx.box(class_name="w-[400px] border-t-2 border-[#1F1300] my-12 bg-[#001B2E]"),
        rx.text("Feel free to explore our Products",align="center",size="7",class_name={"font-semibold pb-4 text-[#1F1300]"}),
        rx.flex(
            card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),card(),
            class_name={"w-full gap-8 overflow-x-scroll py-10"},
        ),
        direction="column",justify="center",class_name="items-center",
    )