import json
from datetime import datetime

from database import db, Item, convertToDict
from flask import Blueprint, make_response, request, render_template, session

from backend.util import addCart, viewCart
from backend.nearest_location_search_with_distance import get_closest_store

cart = Blueprint("api/cart", __name__, url_prefix="/api/cart")

@cart.route("/add/<item_name>", methods=["GET"])
def addToCart(item_name):
    n = request.args.get("n", 1)
    try:
        n = int(n)
    except ValueError:
        return make_response(({"message": "n argument not an integer.", "success": False}, 400))
    if n < 0:
        return make_response(({"message": "n argument must be non-negative or omitted.", "success": False}, 400))

    addCart(item_name, n)
    return make_response({"message": "OK", "success": True})

@cart.route("/view", methods=["GET"])
def viewCurrentCart():
    return make_response(viewCart())

@cart.route("/breakdown", methods=["GET"])
def viewCartBreakdown():
    method = request.args.get("method", "car").lower()
    if method == "car":
        method = "driving"
    elif method == "bicycle":
        method = "bicycling"
    cart = viewCart()
    breakdownStores = {}
    for item in cart:
        itemQuery = Item.query.filter(Item.item_name == item)
        details = [convertToDict(it) for it in itemQuery.all()]
        for detail in details:
            store = detail["store"]
            if store not in breakdownStores:
                breakdownStores[store] = {"name": store, "items": [], "subtotal": 0.0}
            detail["quantity"] = cart[item]
            breakdownStores[store]["items"].append(detail)
            breakdownStores[store]["subtotal"] += cart[item] * detail["item_price"]

    location = session.get("location", "n/a")
    for store in breakdownStores:
        breakdownStores[store]["subtotal"] = round(breakdownStores[store]["subtotal"], 2)
        if location != "n/a":
            res = get_closest_store(location, store, method)
            breakdownStores[store]["distance"], breakdownStores[store]["time"] = res[2], res[3]
        else:
            breakdownStores[store]["distance"], breakdownStores[store]["time"] = "n/a", "n/a"

    ret = {"stores": list(breakdownStores.values())}
    return make_response(ret)
