from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Signup(BaseModel):
    name: str
    email: str
    password: str

my_signup_data = [{"id": 1, "name": "suresh", "email": "ydv@gmail.com", "password": "password"},
                {"id": 2, "name": "raina", "email": "ydvsuresh@gmail.com", "password": "pass"}]

@app.get("/")
async def root():
    return {"message": "Welcome to API Development"}


@app.get("/posts")
async def get_post():
    return {"data": "This is your post"}

@app.post("/signup")
async def create_signup(items: Signup):
    print(items.email)
    print(items)
    print(items.dict())
    return items

@app.post("/data/append")
def data_append(items: Signup):
    data_dict = items.dict()
    data_dict['id'] = randrange(0, 100)
    my_signup_data.append(data_dict)
    return {"data": data_dict}