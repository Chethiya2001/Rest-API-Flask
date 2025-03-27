import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import stores

blp = Blueprint("stores", __name__, discription="Operations on Stores")


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

    def post(self):
        data = request.get_json()
        store_id = uuid.uuid4().hex
        store = {**data, "id": store_id}
        stores[store_id] = store
        return store, 201
