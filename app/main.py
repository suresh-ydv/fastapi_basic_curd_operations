from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Signup(BaseModel):
    name: str
    email: str
    password: str

signup_db = [{"id": 1, "name": "suresh", "email": "ydv@gmail.com", "password": "password"},
                {"id": 2, "name": "raina", "email": "ydvsuresh@gmail.com", "password": "pass"}]


def find_signup(id):
    for i in signup_db:
        if i["id"] == id:
            return i

def find_index_singup(id):
    for i, p in enumerate(signup_db):
        if p["id"] == id:
            return i    

@app.get("/")
async def root():
    return {"message": "Welcome to API Development"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your post"}

@app.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_signup(items: Signup):
    print(items.email)
    print(items)
    print(items.dict())
    return items

@app.post("/data/append")
def data_append(items: Signup):
    data_dict = items.dict()
    data_dict['id'] = randrange(0, 100)
    signup_db.append(data_dict)
    return {"data": data_dict}

# @app.get("/signup/{id}")
# def get_signup(id: int, response: Response):
#     data = find_signup(id)
#     if not data:
#         # response.status_code = 404   --> Instead of hard coding
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": f"The data of id: {id} was not found"}
#     return {"signup_details": data}


'''More Clearner then above comment router'''
@app.get("/signup/{id}")
def get_signup(id: int):
    data = find_signup(id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"The data of id: {id} was not found")
    return {"signup_details": data}

@app.delete("/signup/index/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_singup(id: int):
    index = find_index_singup(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Id {id} does not exist")
    
    signup_db.pop(index)
    # return {"message": "Data is deleted successfully"}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/signup/update/{id}")
def update_signup(id: int, details: Signup):
    index = find_index_singup(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Id {id} does not exist")

    # print(details)
    signup_details = details.dict()
    signup_details['id'] = id
    signup_db[index] = signup_details
    return {"data": signup_db}