import json
import bcrypt
from datetime import datetime

from database import db, Item, convertToDict
from flask import Blueprint, make_response, request, render_template, jsonify
from sqlalchemy import text

item = Blueprint("api/item", __name__, url_prefix="/api/item")

@item.route("/", methods=["GET"])
def getItems():
    id = request.args.get("item_id")
    if id is not None:
        try:
            id = int(id)
        except ValueError:
            return make_response(("id argument not an integer", 400))
        item = Item.query.filter(Item.item_id == id)
    else:
        item = Item.query
        name = request.args.get("name")
        brand = request.args.get("brand")
        category = request.args.get("category")
        store = request.args.get("store")
        if name is not None:
            for subname in name.split(" "):
                item = item.filter(text("LOWER(item_name) LIKE '%' || '" + subname.lower() + "' || '%'"))
        if brand is not None:
            item = item.filter(Item.brand == brand)
        if category is not None:
            item = item.filter(Item.item_category == category)
        if store is not None:
            item = item.filter(Item.store == store)
    group = request.args.get("group", True)
    if group and group != "false" and group != "0":
        d = {}
        for it in item.all():
            it = convertToDict(it)
            if it["item_name"] not in d:
                entry = {"item_name": it["item_name"], "item_category": it["item_category"], "url": it["url"], "price_range": [], "stores": []}
                d[it["item_name"]] = entry
            d[it["item_name"]]["price_range"].append(it["item_price"])
            if it["store"] not in d[it["item_name"]]["stores"]:
                d[it["item_name"]]["stores"].append(it["store"])
        for key in d:
            d[key]["price_range"] = "${:.2f} - ${:.2f}".format(min(d[key]["price_range"]), max(d[key]["price_range"]))
            d[key]["stores"] = ", ".join(d[key]["stores"])
        item = [it for it in d.values()]
    else:
        item = [convertToDict(it) for it in item.all()]

    n = request.args.get("top_n")
    if n is not None:
        try:
            n = int(n)
        except ValueError:
            return make_response(("top_n argument not an integer", 400))
        if abs(n) < len(item):
            item = item[:n]

    resp = {"items": item}
    return make_response(resp)
