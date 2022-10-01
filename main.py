from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import uvicorn

# create instance of FastAPI
app = FastAPI()
url = "https://api.ultramsg.com/instance14131/messages/chat"


# mandatory to return something in fucntion
@app.get('/')
def index():
    print("Send Message")
    return {"Message":"Hello world"}


@app.get('/blog/{id}')
def blog(id:int):
    return {"Name":id}

@app.get('/blog')
def blog(limit:int =10,published:bool=True,sort:Optional[int]=None):
    if published:
        return {"Data":f"{limit} published blogs from the Database"}
    else:
        return {"Data":f"{limit} blogs from the Database"}


class Blog(BaseModel):
    # data:Json
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
async def get_body(request: Request):
    data=await request.json()
    print(data)
    payload = f"token=j6zub8czi2qjp57p&to=+917720063009,&body=Sent Data&priority=10&referenceId="
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    requests.request("POST", url, data=payload, headers=headers)
    # await print(request.json())
    return ""



if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
    # uvicorn.run(app=app,host="127.0.0.1",port=8000,reload=True)