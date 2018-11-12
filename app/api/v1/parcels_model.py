"""Parcels model"""
from .models import UserModel
orders = [{
    "order_id":"100",
    "pickup_location":"nakuru",
    "destination":"nairobi",
    "price":"1400",
    "user_id":"2"
}, {
    "order_id":"104",
    "pickup_location":"isiolo",
    "destination":"narok",
    "price":"1400",
    "user_id":"5"
}, {
    "order_id":"102",
    "pickup_location":"kisumu",
    "destination":"mombasa",
    "price":"1400",
    "user_id":"2"
}, {
    "order_id":"103",
    "pickup_location":"sultan hamud",
    "destination":"diani",
    "price":"1400",
    "user_id":"2"
}]

class Parcels:
    """The Parcels class"""

    def __init__(self):
        self.db = orders
        self.order_status = 'pending'

    def create_orders(self, pickup_location, destination, price, user_id):
        """Create orders"""
        payload = {
            'order_id' : len(orders) + 1,
            'pickup_location': pickup_location, 
            'destination' : destination,
            'price' : price, 
            'user_id' : user_id   
        }
        prcl = self.db.append(payload)
        return prcl

    def get_all_orders(self):
        """Return all orders"""
        return self.db

    def get_specific_order(self, order_id):
        """Return a specific order"""
        order = [order for order in self.db if order['order_id'] == str(order_id)]
        return order[0]

    def get_orders_by_specific_user(self, user_id):
        """Return all orders by a specific user"""
        user_orders = []
        for order in self.db:
            if order['user_id'] == str(user_id):
                user_orders.append(order)
        return user_orders 

    def cancel_order(self, order_id):
        """Cancel an order"""
        order = [order for order in self.db if order['order_id'] == str(order_id)]
        order[0]['status'] = 'cancelled'
        return order
