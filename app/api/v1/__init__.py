from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v1.views import AllOrders, OneOrder, GetOneOrder, UserParcels

version1 = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(version1)

api.add_resource(OneOrder, '/parcel', strict_slashes=False)
api.add_resource(AllOrders, '/parcels', strict_slashes=False)
api.add_resource(GetOneOrder, '/parce/<int:order_id>', strict_slashes=False)
api.add_resource(UserParcels, '/parc/<int:user_id>', strict_slashes=False)
