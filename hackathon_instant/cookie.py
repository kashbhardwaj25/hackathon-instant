import reflex as rx

class CookieState(rx.State):
    custom_cookie: str = rx.Cookie(
        name='access_token',path='/',same_site='lax',secure=False
    )

    def obtain_cookie(self)->None:
        print("<><><><>",self.custom_cookie)
        return self.custom_cookie