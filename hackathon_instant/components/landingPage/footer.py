import reflex as rx

def footer() -> rx.Component:
    return rx.flex(
                rx.flex(
                  rx.flex(rx.image(src="logo.png",height="40px",width="40px"),
                   rx.text("Craftify Pvt. Limited", class_name="font-bold hidden md:block"),
                   class_name="items-center gap-3"),
                   rx.flex(rx.text("Privacy"),
                         rx.text("Terms"),
                         class_name="lg:gap-8 gap-4 flex font-semibold"),
                   class_name="lg:mx-[120px] mx-2 py-4 w-full items-center",
                   justify="between"),
                   class_name="bg-[#EAE3F8] w-full mt-20 text-[#4F2956]",
              )