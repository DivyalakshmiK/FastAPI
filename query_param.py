from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

l = [1,2,3,4,5,6,7,8,9,10]

@app.get ("/items")
def get_all_items(start:int, limit:int):
    return l[start:start+limit]

#Optional query param

@app.get ("/item/{item_id}")
def checkifq(item_id : int ,q: str | None = None):
    if q: return [item_id,"Q is present"]
    return "q is absent bro"

#boolean and multiple param

@app.get("/multi/{itemid}") 
def check_multi(itemid:int, second:int | None = None, desc:bool = False):
    item = {"itemid":itemid}

    if second: item.update({"q":second})
    if desc: return "You have description and following!!",item
    return item

#create post request

class Item(BaseModel):
    uid :int
    name:str
    email: str |None

@app.post("/create/")
def create_item(item:Item):
    return item

@app.post("/create/{item_id}")
def create_by_itemid(item_id:int,item:Item):
    return {"hello": item_id, **item.dict()}

#trying out branches


