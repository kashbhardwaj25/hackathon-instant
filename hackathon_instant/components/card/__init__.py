import reflex as rx

def card()-> rx.Component:
    return rx.container(rx.image(src={"https://img0.junaroad.com/uiproducts/19126280/zoom_0-1673529652.jpg"}, width="700px",class_name={"p-3"}, height="auto"),rx.text("Mens Printed Casual Shirt",size="3",align="center",class_name="text-white"),
                         rx.flex(
                             rx.text("S",class_name="text-white opacity-40 hover:opacity-100"),
                             rx.text("M",class_name="text-white opacity-40 hover:opacity-100"),
                             rx.text("L",class_name="text-white opacity-40 hover:opacity-100"),
                             rx.text("XL",class_name="text-white opacity-40 hover:opacity-100"),justify="center",class_name="gap-6 text-sm"),class_name={"bg-slate-800 cursor-pointer max-w-[250px] rounded-xl w-full h-[380px] relative"})

