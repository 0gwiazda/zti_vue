import database as db
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Person(BaseModel):
    fname: str
    lname: str
    city: str
    email: str
    tel: str

def convert_to_json(data):
    if len(data) < 6:
        print("Invalid data")
        return {}
    
    return {"id": data[0], "fname": data[1], "lname": data[2], "city": data[3], "email": data[4], "tel": data[5]}

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/person")
async def get_person():

    res = db.view_people()

    result = convert_to_json(res)

    return result

@app.post("/person")
async def add_person(person: Person):

    to_send = [
        person.fname,
        person.lname,
        person.city,
        person.email,
        person.tel
    ]

    res = db.add_person(to_send)

    if res != 0:
        return {}
    
    return {"message": "success"}

@app.put("/person")
async def edit_person(fname: str, lname: str, person: Person):
    
    to_params = [
        fname,
        lname
    ]

    to_data = [
        person.fname,
        person.lname,
        person.city,
        person.email,
        person.tel
    ]

    res = db.edit_person(to_params, to_data)
    
    if res != 0:
        return {}

    return {"message": "success"}

@app.delete("/person")
async def del_person(fname: str, lname: str):

    to_params = [
        fname,
        lname
    ]

    res = db.del_person(to_params)

    if res != 0:
        return {}

    return {"message": "success"}