import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import stores
from schema import StoreSchema

blp = Blueprint("stores", __name__)


@blp.route("/stores/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id], 200
        except KeyError:
            abort(404, message="Store Not Found!.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store Deleted"}
        except KeyError:
            abort(404, message="Store Not Found!.")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    @blp.arguments(StoreSchema)
    def post(self, data):
        store_id = uuid.uuid4().hex
        store = {**data, "id": store_id}
        stores[store_id] = store
        return store, 201
