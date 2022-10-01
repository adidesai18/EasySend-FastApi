# FastApi

## Requirments

1. Install fastapi package
2. Install uvicorn package
3. Create main.py file
4. Start server by `uvicorn fileName:instanceName --reload`
5. ngrok command `ngrok http 127.0.0.1:8000`

## Path Parameters

dynamic routing:-

    @app.get('/blog/{id}')
    def blog(id:int):
        # provide type for parameter,default is str
        return {"Name":id}

FastApi is procedure means it finds path strp by step,this means below code should be above of above code

    @app.get('/blog/unpublished')
    def unpublished():
        return {"data":"returns all unpublished blogs"}

## API docs

For testing Api just code to:-

    endpoint/docs

or

    endpoint/redoc

## Query Parameter

Query parameter doesn't see but we can use in operation function

    @app.get('/blog')
    def blog(limit:int=10,published:bool=True,sort:Optional[int]=None):
        if published:
            return {"Data":f"{limit} published blogs from the Database"}
        else:
            return {"Data":f"{limit} blogs from the Database"}

## Request Parameter

    from pydantic import BaseModel
    class Blog(BaseModel):
        # data:Json
        title:str
        body:str
        published:bool


    @app.post('/blog')
    def increate_blog(request:Blog):
        return {"Message":request}

## Debugging

1. Add break point
2. open command pallet(shift+command+p)
3. type debug:Restart
4. FastApi framework

To chnage local port:-

    import uvicorn
    if__name__=="__main__":

        uvicorn.run("main:app",host="127.0.0.1",port=8000reload=True)

        # uvicorn.run(app=app,host="127.0.0.1",port=8000)

## Pydantic Schemas

## Reference

1. To take random json as body:

   https://stackoverflow.com/questions/64379089/how-to-read-body-as-any-valid-json
