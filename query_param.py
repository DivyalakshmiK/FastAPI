from fastapi import FastAPI

app = FastAPI()

l = [1,2,3,4,5,6,7,8,9,10]

@app.get ("/items")
def get_all_items(start:int, limit:int):
    return l[start:start+limit]
