from fastapi import FastAPI

# create instance of FastAPI
app = FastAPI()


# mandatory to return something in fucntion
@app.get('/')
def index():
    print("Send Message")
    return {"Message":"Hello world"}



@app.get('/blog/{id}')
def blog(id:int):
    return {"Name":id}



@app.post('/')
def index():
    print("Send Message")
    return {"Message":"Hello world"}