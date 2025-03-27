import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schema import ItemsSchema, ItemUpdateSchema

blp = Blueprint("items", __name__)


@blp.route("/items/<string:item_id>")
class Store(MethodView):
    def get(self, item_id):
        try:
            return items[item_id], 200
        except KeyError:
            abort(404, message="item Not Found!.")

    @blp.arguments(ItemUpdateSchema)
    def put(self, item_id, item_data):
        try:
            item = items[item_id]
            item != item_data
            return item
        except KeyError:
            abort(404, message="Item Not Found!.")

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

    @blp.arguments(ItemsSchema)
    def post(self, item_data):
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(404, message="Store Not Found!.")
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[id] = item
        return item, 201
