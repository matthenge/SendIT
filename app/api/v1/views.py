from flask import jsonify, make_response, request
from flask_restful import Resource
from.parcels_model import Parcels

parcel = Parcels()

"""Version 1 views"""

class OneOrder(Resource):
    """Class for single order endpoints"""
    def post(self):
        """Create order endpoint"""
        data = request.get_json()
        pickup_location = data['pickup_location']
        destination = data['destination']
        price = data['price']

        parcel.create_orders(pickup_location, destination, price)
        return {
            "message": "Order placed Successfully"
        }, 201
