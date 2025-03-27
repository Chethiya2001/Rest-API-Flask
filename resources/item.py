import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items

blp = Blueprint("items", __name__, discription="Operations on Items")


@blp.route("/items/<string:item_id>")
class Store(MethodView):
    def get(self, item_id):
        try:
            return items[item_id], 200
        except KeyError:
            abort(404, message="item Not Found!.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "item Deleted"}
        except KeyError:
            abort(404, message="Item Not Found!.")


@blp.route("/items")
class StoreList(MethodView):
    def get(self):
        return {"Items": list(items.values())}

    def post(self):
        item_data = request.get_json()
        if item_data["store_id"] not in items:
            abort(404, message="Store Not Found!.")
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[id] = item
        return item, 201
