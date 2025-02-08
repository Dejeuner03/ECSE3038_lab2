from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

data = []

class person(BaseModel):
    name:str
    occupation: str
    address: str
        
# Post Handler Request: to add new people to the existing data list
@app.post("/person")
def create_new_person(person_request: person):
    if not all([person_request.name, person_request.occupation, person_request.address]):
        return {"success": False, "result": {"error_message": "invalid request"}}
    person_json = jsonable_encoder(person_request)
    data.append(person_json)
    return {"success":True, "result": person_json}
    

#Get Handler Request to retrieve all existing people in the list
@app.get("/person")
def get_existing_person():
    return data