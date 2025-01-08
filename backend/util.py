from database import db
from flask import session

def createCart():
    if "cart" not in session:
        session["cart"] = {}

def viewCart():
    createCart()
    return session["cart"]

def addCart(item_name, n):
    createCart()
    cart = viewCart()
    if item_name not in cart:
        cart[item_name] = 0
    cart[item_name] += n
