from .models import UserModel
orders = []
"""Parcels model"""

class Parcels:
    """The Parcels class"""

    def __init__(self):
        self.db = orders
        self.order_status = 'pending'

    def create_orders(self, pickup_location, destination, price):
        """Create orders"""
        payload = {
            'order_id' : str(len(orders) + 1),
            'pickup_location': pickup_location, 
            'destination' : destination,
            'price' : price,    
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
