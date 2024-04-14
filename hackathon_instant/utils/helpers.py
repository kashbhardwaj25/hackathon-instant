import os
from fastapi import HTTPException, Request
import jwt
import requests
import json

SECRET_KEY = os.getenv('SECRET_KEY')
GPT_KEY = os.getenv('GPT_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def get_current_user(token:str):

    print(token,'token')
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=403, detail="Invalid authentication credentials")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Invalid authentication token")
    
    return user_id



async def get_gpt_response(prompt:str,product:str):

    final_call = prompt + "  " +f"here is the html string change the whole text content and the colours of html for the hypothetical product of this category {product} and add some features by yourself so give full html code with correct placement of /n and give me complete html code with changes only give only html code no text strictly but strictly dont change the html structure just text, images and colours for whole html"
    url = "https://api.openai.com/v1/chat/completions"
    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": final_call
        },
        
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {GPT_KEY}",}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()