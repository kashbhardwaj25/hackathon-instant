import reflex as rx

from hackathon_instant.cookie import CookieState
from hackathon_instant.models.user import store_list


class FetchStores(rx.State):
     
    stores = []

    async def fetch_store(self):
        mycookie = await self.get_state(CookieState)
        self.stores = await store_list(mycookie.custom_cookie[0])

    def get_stores(self):
        return self.stores

def header() -> rx.Component:
      
      fetched_stores = FetchStores.get_stores
      print(fetched_stores)
            

      return rx.flex(
        rx.flex(
             rx.image(src="logo.png", width="50px", height="50px"),
             rx.text("Craftify", class_name="text-2xl font-semibold hidden md:block text-[#4F2956]"),
             spacing="3",
             class_name="items-center flex"
        ),
        rx.button("Login", color_scheme="violet",width="100px",size="3",on_click=rx.redirect("/login")),
        rx.button("Get Stores", color_scheme="violet",width="100px",size="3",on_click={FetchStores.fetch_store}),
        justify="between",
        class_name="px-2 md:px-[80px] py-4 bg-[#EAE3F8] flex items-center"
        )