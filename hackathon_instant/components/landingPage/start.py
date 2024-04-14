import reflex as rx 

def start() -> rx.Component:
    return  rx.flex(
                rx.flex(
                    rx.flex(
                     rx.box("Start Building",
                           rx.text("TODAY", class_name="text-[#644dc4] lg:text-5xl text-3xl font-bold mt-2"),
                           class_name="lg:text-5xl text-3xl mt-4 text-[#4F2956] flex flex-col lg:flex-row items-center lg:gap-3"),
                     rx.box("Sign up now to unlock the power of Craftify and start creating high-converting Shopify pages and sections without any code",
                            class_name="mt-4 mb-6 text-lg font-medium text-center lg:text-left"),
                     rx.button("Sign Up", size="3", color_scheme="violet"),
                     justify="center",
                     class_name="flex flex-col lg:w-[50%] w-full justify-center"),
                     rx.image(src="start.jpg",class_name="lg:w-[45%] w-full mt-12 lg:mt-0"),
                    class_name="lg:mx-[80px] px-6 lg:w-[80%] w-full justify-between items-center flex flex-col lg:flex-row",
                    justify="between",
                    align="center"
                ),
                    justify="center",
                    class_name="w-full  lg:mt-28 mt-14")