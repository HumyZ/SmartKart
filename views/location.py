import json
from flask import Blueprint, make_response, request, session

location = Blueprint("api/location", __name__, url_prefix="/api/location")

@location.route("/", methods=["POST", "GET"])
def loc():
    if request.method == "GET":
        return session.get("location", "n/a")
    # POST Request
    data = json.loads(request.get_data(as_text=True))
    resp = {}
    if "location" not in data:
        resp["success"] = False
        resp["message"] = "location data not provided in POST request."
        return make_response((resp, 400))

    session["location"] = data["location"]
    resp["success"] = True
    resp["message"] = "Location updated successfully."
    return make_response(resp)
