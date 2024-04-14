from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/get-cookie-from-header")
async def get_cookie_from_header(request: Request):
    cookie_header = request.headers.get('Cookie')
    if cookie_header:
        cookies = parse_cookie_header(cookie_header)
        access_token = cookies.get('access_token', None)
        if access_token:
            return {"Access Token": access_token}
        else:
            return {"Error": "Access token not found in cookies"}
    else:
        return {"Error": "No cookie header found"}

def parse_cookie_header(cookie_header: str):
    """A simple parser to extract cookies from the cookie header"""
    cookies = {}
    pairs = cookie_header.split('; ')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            cookies[key] = value
    return cookies