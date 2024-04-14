import reflex as rx
from .contact_us import contact_us
from .header import header
from .crousel import crousel
from .feature_section import feature_section
from .hero_section import hero_section
from .footer import footer

def card()-> rx.Component:
    return rx.container(rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"}, width="700px",class_name={"p-3"}, height="auto"),rx.text("Mens Printed Casual Shirt",size="3",align="center",class_name="text-white"),
                         rx.flex(
                             rx.text("S",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("M",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("L",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),
                             rx.text("XL",class_name="text-[#F0E7D8] opacity-40 hover:opacity-100"),justify="center",class_name="gap-6 text-sm"),class_name={"bg-[#001B2E] drop-shadow-lg cursor-pointer max-w-[250px] rounded-xl w-full h-[380px]"})


def template() -> rx.Component:
    return rx.flex(
        header(),
        hero_section(),
        crousel(),
        feature_section(),
        contact_us(),
        footer(),
        direction="column",
    )

