import reflex as rx

def team() -> rx.Component:

    return rx.flex(
                rx.flex(
                    rx.image(src="team.jpg",class_name="lg:w-[55%] w-full"),
                    rx.flex(
                     rx.box("WHO WE ARE", class_name="text-[#644dc4] font-bold"),
                     rx.box("The passion and purpose behind",class_name="lg:text-5xl text-3xl mt-4 text-[#4F2956]"),
                        rx.text("Craftify", class_name="text-[#644dc4] lg:text-5xl text-3xl font-bold mr-2"),
                        rx.box("Founded by a team of e-commerce enthusiasts, Craftify was born out of a desire to simplify the process of building Shopify pages without sacrificing quality or flexibility.",
                            class_name="my-4 lg:text-lg font-medium"),
                     justify="center",
                     class_name="flex flex-col lg:w-[40%] w-full justify-center text-center lg:text-left"),
                    class_name="lg:mx-[80px] mx-2 lg:w-[90%] w-full justify-between items-center gap-[12px] flex-col lg:flex-row",
                    justify="between",
                    align="center"
                ),
                justify="center",
                class_name="w-full  lg:mt-20 mt-12")