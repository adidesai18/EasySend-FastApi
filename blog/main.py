from blog.Schemas import Blog
from fastapi import Request, FastAPI

app = FastAPI()

# @app.post('/blog')
# def increate_blog(request:Blog):
#     return request



@app.post('/blog')
async def get_body(request: Request):
    data=await request.json()
    print(data)
    # await print(request.json())
    return data