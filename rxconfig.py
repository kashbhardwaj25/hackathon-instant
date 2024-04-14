import reflex as rx # type: ignore

config = rx.Config(
    app_name="hackathon_instant",
    db_url = "postgresql://postgres:postgres@localhost:5432/hackathon"
)