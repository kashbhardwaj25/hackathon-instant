from sqlalchemy import Column, DateTime
from datetime import datetime
from sqlmodel import Field
import reflex as rx

class StoreData(rx.Model, table=True):
     id: str = Field(primary_key = True, nullable = False, unique = True,)
     store_name: str = Field(nullable=False, unique = True)
     access_token: str = Field(nullable=True)    
     is_app_install: bool = Field(nullable=False, default=False)
     created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
     updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

class QueryStore(rx.State):
    name: str

    def get_users(self):
        with rx.session() as session:
            self.users = session.exec(
                StoreData.select.where(
                    StoreData.store_name.contains(self.name)
                ).all()
            )