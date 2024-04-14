import reflex as rx

def benefits() -> rx.Component:
    return rx.flex(rx.flex(
                    rx.box("BENEFITS", class_name="text-[#644dc4] font-bold"),
                    rx.box("We Provide Best", class_name="lg:text-5xl text-3xl mt-4 text-[#4F2956]"),
                    rx.flex(
                        rx.text("Solution", class_name="text-[#644dc4] lg:text-5xl text-3xl font-bold mr-2"),
                        rx.text("for you", class_name="text-[#4F2956] lg:text-5xl text-3xl ml-2"), class_name="flex gap-3"),
                    rx.flex(
                        rx.flex(
                            rx.box(
                                rx.image(src="conversion.png", class_name="object-contain"),
                                class_name="p-2 lg:h-[120px] lg:w-[120px] h-[80px] w-[80px] rounded-full p-3 bg-[#EAE3F8]"),
                            rx.flex(
                                rx.box("High-Conversion", class_name="text-[#4F2956] text-xl font-bold"),
                                rx.box("Our templates are optimized for conversions, helping you drive more sales and grow your business",
                                class_name="mt-2 text-center"),
                                class_name="flex flex-col gap-2 items-center justify-center"
                                ),
                            class_name="flex flex-col gap-4 items-center"),
                        rx.flex(
                            rx.box(
                                rx.image(src="time.png", class_name="object-contain"),
                                class_name="p-2 lg:h-[120px] lg:w-[120px] h-[80px] w-[80px] rounded-full p-5 bg-[#EAE3F8]"),
                            rx.flex(
                                rx.box("Time-Saving",
                                class_name="text-[#4F2956] text-xl font-bold"),
                                rx.box("Save hours of time with our intuitive interface, allowing you to focus on what matters most",
                                class_name="mt-2 text-center"),
                                class_name="flex flex-col gap-2 items-center justify-center"
                                ),
                             class_name="flex flex-col gap-4 items-center"),
                        rx.flex(
                            rx.box(
                                rx.image(src="customize.png", class_name="object-contain"),
                                class_name="p-2 lg:h-[120px] lg:w-[120px] h-[80px] w-[80px] rounded-full p-6 bg-[#EAE3F8]"),
                            rx.flex(
                                rx.box("Customization",
                                class_name="text-[#4F2956] text-xl font-bold"),
                                rx.box("Tailor your pages and sections to match your brand perfectly, with no technical expertise needed",
                                class_name="mt-2 text-center"),
                                class_name="flex flex-col gap-2 items-center justify-center"
                                ),
                             class_name="flex flex-col gap-4 items-center"),
                        class_name="justify-between lg:w-[85%] w-full lg:mt-16 mt-8 lg:gap-20 gap-10 flex-col lg:flex-row",
                        justify="between"
                    ),
                class_name="flex flex-col lg:mx-[80px] mx-2 items-center "
                ),class_name="bg-[#F7F5FC] py-8 mt-20 sm:mt-0")