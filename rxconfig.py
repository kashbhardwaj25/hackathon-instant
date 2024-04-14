import reflex as rx # type: ignore

config = rx.Config(
    app_name="hackathon_instant",
    db_url = "postgresql://postgres:1972@localhost:5432/hackathon"
)