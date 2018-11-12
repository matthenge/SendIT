"""Version 1 views"""
from flask import jsonify, make_response, request
from flask_restful import Resource
from.parcels_model import Parcels
from.models import UserModel

parcel = Parcels()
users = UserModel()

class OneOrder(Resource):
    """Class for single order endpoints"""
    def post(self):
        """Create order endpoint"""
        data = request.get_json()
        pickup_location = data['pickup_location']
        destination = data['destination']
        price = data['price']
        user_id = data['user_id']

        parcel.create_orders(pickup_location, destination, price, user_id)
        return {
            "message": "Order placed Successfully"
        }, 201

class GetOneOrder(Resource):
    """Specific order endpoints"""
    def get(self, order_id):
        """GET specific order"""
        one_order = parcel.get_specific_order(order_id)
        return {
            "message": "Order retrieved", "Order": one_order
        }, 200
    
    def put(self, order_id):
        """Cancel order"""
        cncl = parcel.cancel_order(order_id)
        return {
            "message": "Order Cancelled", "Order": cncl
        }, 201

class AllOrders(Resource):
    """Class for all order views"""
    def get(self):
        """Return all orders"""
        all_orders = parcel.get_all_orders()
        return {
            "message": "Success", "Orders": all_orders
        }, 200

class UserParcels(Resource):
    """Class for single user operations"""
    def get(self, user_id):
        """Get all orders by a specific user"""
        all_user_orders = parcel.get_orders_by_specific_user(user_id)
        return {
            "message": "user orders", "Orders": all_user_orders
        }, 200
        
class OneUser(Resource):
    """Class for single user operations"""
    def post(self):
        """Create user"""
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        email = data['email']
        password = data['password']

        users.add_users(firstname, lastname, username, email, password)
        return{
            "message": "successful registration"
        }, 201

class GetUser(Resource):
    """Get one user"""
    def get(self, user_id):
        """Get a single user"""
        one_user = users.get_one_user(user_id)
        return {
            "message": "user retrieved", "user": one_user
        }, 200
