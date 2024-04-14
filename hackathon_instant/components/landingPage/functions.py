import reflex as rx

def functions() -> rx.Component:

    return  rx.flex(
                rx.flex(
                    rx.box(
                        rx.flex("Professionally Designed Templates",
                         class_name="ml-[160px] text-[#4F2956] bg-[#EAE3F8] w-40 h-40 rounded-full p-4 items-center justify-center text-center font-semibold"),
                        rx.flex("Responsive Design",
                         class_name="text-[#4F2956] bg-[#EAE3F8] w-40 h-40 rounded-full p-4 items-center justify-center text-center font-semibold"),
                        rx.flex("Seamless Shopify Integration",
                         class_name="ml-[160px] text-[#4F2956] bg-[#EAE3F8] w-40 h-40 rounded-full p-4 items-center justify-center text-center font-semibold"),
                        class_name="lg:flex lg:flex-col gap-8 hidden"
                    ),
                    rx.flex("Discover the Power of Craftify",
                            class_name="text-4xl font-bold text-[#EAE3F8] bg-[#644dc4] rounded-full w-80 h-80 p-5 justify-center items-center text-center"),
                    rx.box(
                        rx.flex("Customization Options",
                         class_name="text-[#4F2956] bg-[#EAE3F8] w-40 h-40 rounded-full p-4 items-center justify-center text-center font-semibold"),
                        rx.flex("Optimized for Conversions",
                         class_name="text-[#4F2956] bg-[#EAE3F8] ml-[160px] w-40 h-40 rounded-full p-4 items-center justify-center text-center font-semibold"),
                        rx.flex("Regular Updates and Support",
                         class_name="text-[#4F2956] bg-[#EAE3F8] w-40 h-40 rounded-full p-4 items-center justify-center text-center font-semibold"),
                        class_name="lg:flex lg:flex-col hidden gap-8"
                    ),
                    class_name="lg:mx-[80px] mx-2 lg:mt-20 w-full gap-12",
                    align="center",
                    justify="center"
                ),
                justify="center",
                class_name="mt-14")