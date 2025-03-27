import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)


# end points
@app.get("/stores")
def getStores():
    return {"stores": list(stores.values())}


@app.post("/stores")
def addStores():
    data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**data, "id": store_id}
    stores[store_id] = store
    return store, 201


@app.post("/item")
def addItem():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        abort(404, message="Store Not Found!.")

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[id] = item
    return item, 201


@app.get("/items")
def getItems():
    return {"Items": list(items.values())}


@app.get("/stores/<string:store_id>")
def getStoreItem(store_id):
    try:
        return stores[store_id], 200
    except KeyError:
        abort(404, message="Store Not Found!.")


@app.get("/items/<string:item_id>")
def getItem(item_id):
    try:
        return stores[item_id], 200
    except KeyError:
        abort(404, message="Item Not Found!.")
