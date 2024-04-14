import reflex as rx

def hero_section() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.box("We are", class_name="lg:text-5xl text-3xl text-[#4F2956] font-semibold"),
            rx.box("CRAFTIFY", class_name="lg:text-8xl text-6xl font-extrabold text-[#644dc4] mt-2"),
            rx.box("Explore Craftify today to start building high-converting landing pages and sections, no-code required",
            class_name="mt-4 mb-8 text-lg font-medium"),
            rx.button("Get Started", size="3", color_scheme="violet"),
            justify="center",
            class_name="flex flex-col h-[80%] w-full lg:w-[50%] justify-center text-center lg:text-left"),
        rx.image(src='illustration.jpg',
                class_name="lg:w-[60%] w-full h-[80%]"),
        class_name="flex mt-[60px] lg:mx-[80px] mx-2 gap-10 flex-col lg:flex-row",
        justify="between")