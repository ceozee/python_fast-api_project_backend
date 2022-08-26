from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    zeenet = 'zee'
    zachnet = 'zach'
    zaelnet = 'zael'

app = FastAPI()

@app.get('/')
async def root():
    return {
        'message': 'Hello World'
    }


#usage of enums (Check class up)
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.zeenet:
        return {
            'model_name': model_name,
            'message': 'Work Mode'
        }

    if model_name == ModelName.zachnet:
        return {
            'model_name': model_name,
            'message': 'School Mode'
        }

    if model_name == ModelName.zaelnet:
        return {
            'model_name': model_name,
            'message': 'Play Mode'
        }


## check file
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {
        'file_path': file_path
    }

## Query Params use /items/?skip=0&limit=10
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


##Optional Params with bool use path /items/zee?short=True
@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {'item_id': item_id}
    if q:
        return {
            "item_id": item_id,
            'q': q
        }

    if not short:
        item.update(
            {'description': 'Short is true'}
        )
    return item


## Required Parameter
@app.get('/items_req/{item_id}')
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


############# POST
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

