import datetime
import reflex as rx

class StoreData(rx.Model, table=True):
    id: str = rx.field(rx.String, primary_key=True, default=rx.UUIDV4)
    store_name: str = rx.field(rx.String, column_name="storeName")
    email: str = rx.field(rx.String)
    access_token: str = rx.field(rx.String, column_name="accessToken")
    is_app_install: bool = rx.field(rx.Boolean, default=False, column_name="isAppInstall")
    created_at: datetime = rx.field(rx.DateTime, default=rx.utcnow, column_name="createdAt")
    updated_at: datetime = rx.field(rx.DateTime, default=rx.utcnow, column_name="updatedAt")
    deleted_at: datetime = rx.field(rx.DateTime, nullable=True, column_name="deletedAt")
