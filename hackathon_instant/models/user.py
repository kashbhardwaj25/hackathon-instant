import os
import uuid
from fastapi import Depends, HTTPException, Request, Response
from pydantic import BaseModel
import jwt
from sqlalchemy import Column, DateTime
from datetime import datetime, timedelta
from sqlmodel import Field
import reflex as rx

# Load environment variables
from dotenv import load_dotenv

from ..utils.helpers import get_current_user

from .store_data import find_user_store
load_dotenv()

# Constants
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class User(rx.Model, table=True):
    id: str = Field(primary_key = True, default=None)
    username: str = Field(unique=True, nullable=False)
    name: str = Field(nullable=False)
    password: str = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))
    

async def signup(name:str, username:str,password:str):
    
    user_id = str(uuid.uuid4())
    new_user = await create_user(user_id, name, username, password)
    
    if new_user:
        access_token = create_access_token(new_user.id)
        
        return {
            "status": "success",
            "status_code": "200",
            "message": "User created successfully",
            "user_id": new_user.id,
            "access_token": access_token,
            "token_type": "bearer"
        }
    else:
        raise HTTPException(status_code=400, detail="User could not be created")

def create_access_token(user_id: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user_id, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt,expire

async def login(username: str,password: str):
    user = await find_user(username)
    
    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(user.id)

    
    return {"message": "Logged in successfully", "access_token": access_token, "token_type": "bearer","status_code": 200}


async def store_list(user_id: str = Depends(get_current_user)):
    stores = await find_user_store(user_id)
    return stores
    
async def create_user(user_id: str, name: str, username: str, password: bool):
    with rx.session() as session:
        new_user = User(id= user_id, name=name, username=username, password=password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
        
async def find_user(username: str):
    with rx.session() as session:
        result = session.exec(User.select().where(User.username == username))
        user =  result.first()
        return user




