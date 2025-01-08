"""
SmartKart

This file contains the logic that will return to the user, the most optimized
trips that have the items from the user's cart. Data from the databases such as
items, prices, stores, addresses, as well as the user's own address will be
factors that return the best optimized trips in terms of cost and time.
"""
from typing import List, Dict


class Item:
    """
    An Item represents an item that can be found in a store.
    The item has the following:
    - item_id: id of this item (unique)
    - item_name: name of this item
    - category: category of this item (ex. dairy)
    - price: cost of one unit of this item (ex. 2.50)
    - store: which store this item belongs to
    - address: address of this item's store
    """

    def __init__(self, item_id: int, item_name: str, category: str,
                 price: float, store: str, address: str):
        self.item_id = item_id
        self.item_name = item_name
        self.category = category
        self.price = price
        self.store = store
        self.address = address


"""
Sample input:
    milk1 = Item(0, "Milk", "Dairy", 1.50, "NoFrills", "123 Sesame St.")
    cookies1 = Item(1, "Cookies", "Snacks", 2.00, "Loblaws", "456 Elmo's World")
    cookies2 = Item(2, "Cookies", "Snacks", 1.59, "FreshCo", "789 Bridle Path")
    milk2 = Item(4, "Milk", "Dairy", 0.99, "FreshCo", "789 Bridle Path")
    cookies3 = Item(5, "Cookies", "Snacks", 1.30, "NoFrills", "123 Sesame St.")
    
    list_trips([milk1, cookies1, cookies2, milk2, cookies3], ["Cookies, Milk"])
    
    
Sample output (using input from above):

    [
    ([cookies3, milk2], 2.29),
    ([cookies2, milk2], 2.58),
    ([cookies3, milk1), 2.80),
    ]
    
"""


def list_trips(db_items: List[Item], cart_items: List[str]) -> List:
    """
    Given db_items, which has the list of items available in the database,
    return at most 3 trips which contain items from db_items that are in
    cart_items ordered from least total cost to most Also return the total cost
    of each trip.
    """


def optimized_trips(db_items: List[Item], cart_items: List[str],
                    user_address: str) -> List:
    """
    Given a database, db_items, which has the list of items alongside the item's
    price, store, etc., return at most 3 trips which contain items from db_items
    that are in cart_items, using user_address as a measure of distance and
    time. Also return the total cost of each trip.
    """

    # Requires Google Maps API (or alternative)
