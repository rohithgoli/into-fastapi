from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # read_item(item_id: int, q: Optional[str] = None): --> Optional[str] is shortcut for Union[str, None]
    #   Mind it, Using Optional does not indicate that the parameter is Optional for the function
    # read_item(item_id: int, q: str | None = None): --> Only available in Python 3.10+
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}