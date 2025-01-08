import json
import bcrypt
from datetime import datetime

from database import User, Role, db
from flask import Blueprint, request, render_template, current_app, jsonify
from flask_user import roles_required, current_user, UserManager
from flask_login import login_user

login = Blueprint("api/login", __name__, url_prefix="/api/login")

@login.route("/register", methods=["POST"])
def register():
    data = json.loads(request.get_data(as_text=True))
    resp = {}
    email = data["email"]
    pw = bytes(data["password"], 'utf-8')
    if not User.query.filter(User.email == email).first():
        salt = bcrypt.gensalt()
        user = User(
            email=email,
            password=bcrypt.hashpw(pw, salt),
            last_login=datetime.now()
        )
        role = Role.query.filter(Role.name == "User").first()
        if role:
            user.roles.append(role)
        else:
            user.roles.append(Role(name='User'))
        db.session.add(user)
        db.session.commit()
        resp["success"] = True
        resp["message"] = "User successfully created."
    else:
        resp["success"] = False
        resp["message"] = "A User already exists with that email."
    return jsonify(resp)

@login.route("/", methods=["POST"])
def loginToApp():
    resp = {}
    data = json.loads(request.get_data(as_text=True))
    username = data["email"].lower()
    pw = bytes(data["password"], 'utf-8')
    user = User.query.filter(User.email == username).first()
    if user is not None and bcrypt.checkpw(pw, user.password):
        login_user(user)
        resp["success"] = True
        resp["message"] = "User successfully logged in."
    else:
        resp["success"] = False
        resp["message"] = "Could not find a user with those credentials."
    return jsonify(resp)
