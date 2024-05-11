import database as db
import json
from fastapi import FastAPI, HTTPException
from fastapi import Response
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
    res = {"people": []}
    for d in data:
        res["people"].append({"id": d[0], "fname": d[1], "lname": d[2], "city": d[3], "email": d[4], "tel": d[5]})

    return res

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
async def edit_person(first_name: str, last_name: str, person: Person):
    
    to_params = [
        first_name,
        last_name
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