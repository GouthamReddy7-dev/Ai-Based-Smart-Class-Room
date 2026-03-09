from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app=FastAPI()
a=1
b=2

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    #allow_methods=["*"],
    #allow_headers=["*"],
    )

class UserData(BaseModel):
    name: str
    password: str
    email: str

@app.post("/register")
def getdata(userdata:UserData):
    name=userdata.name
    passw=userdata.password
    emails=userdata.email
    print(name)
    print(passw)
    print(emails)
    return {
        "a":a,
        "b":b
    }
#to run uvicorn FileName:app --reload
