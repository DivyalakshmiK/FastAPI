from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

@app.get("/")
def simple_hello():
    return {"message": "Hello, world!!"}

@app.get("/name/{your_name}")
def say_my_name(your_name: str):
    return {"Your name is": your_name}

@app.get("/number/{num}")
def guess_my_fav_number(numb: int, hello="hii"):
    return {"Your favourite number is": numb,
            "Message for you": hello}

@app.get("/gender/{gender}")
async def your_gender(gender: Gender):
    if gender == Gender.male: return {"You're a male"}
    elif gender == Gender.female: return ("You're a female")
    else: return ("Yess, finally a creative one!! But idk what it tho :( ")

@app.get("/file/{filepath:path}")
def find_your_file(filepath: str):
    return {"Your file is in" : filepath}

@app.get("/yourbias/{bias}")
def find_my_bias(bias:str):
    return{"Found your bias" : bias}


