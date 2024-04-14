import os
import uuid
from fastapi import HTTPException, Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import jwt
from sqlalchemy import Column, DateTime
from datetime import datetime, timedelta
from sqlmodel import Field
import reflex as rx

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Constants
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class Signup(BaseModel):
    name: str
    username: str
    password: str

class User(rx.Model, table=True):
    id: str = Field(primary_key = True, default=None)
    username: str = Field(unique=True, nullable=False)
    name: str = Field(nullable=False)
    password: str = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))
    

async def signup(payload: Signup, response: Response):
    name, username, password = payload.name, payload.username, payload.password
    
    user_id = str(uuid.uuid4())
    new_user = await create_user(user_id, name, username, password)
    
    if new_user:
        access_token = create_access_token(new_user.id)
        
        response.set_cookie(
            key="jwt_token", 
            value=access_token,
            max_age=3600,
            httponly=True,
            path='/'
        )
        
        return {
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

def get_current_user(request: Request):
    token = request.cookies.get("jwt_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid JWT token")
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=401, detail="Invalid JWT token") from e
    return user_id


async def login(username: str, password: str):
    user = await find_user(username)
    
    if not user or user.password != password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    # response.set_cookie(key="access_token", value=access_token, httponly=True, max_age=1800)  # Expires in 30 minutes
    return {"access_token": access_token, "token_type": "bearer"}
    
    
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
    
async def set_cookie(response: Response):
    print("Setting cookie...")
    response.set_cookie(key="mycookie", value="the cookie value", httponly=True, max_age=1800)
    print("Cookie should be set now.")
    return {"message": "Cookie is set"}


