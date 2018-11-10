import unittest
from app import create_app
import json
     
class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app

        self.order = {
            "order_id":"100",
            "pickup_location":"nakuru",
            "destination":"nairobi",
            "price":"1400",
            "user_id":"5"

        }
    def test_post(self):
        response = self.client.post('/api/v1/parcel', data=json.dumps(self.order), content_type='application/json')
        result=json.loads(response.data.decode())
        self.assertEqual(result["message"],"Order placed Successfully", msg="Error: Not equal")
        self.assertEqual(response.status_code, 201)

    def test_get_one(self):
        response = self.client.get('/api/v1/parce/100')
        result=json.loads(response.data.decode())
        self.assertEqual(result["message"], "Order retrieved", msg="Order not retrieved" )
        self.assertEqual(response.status_code, 200)

    def test_put_one(self):
        response = self.client.put('/api/v1/parce/100')
        result=json.loads(response.data.decode())
        self.assertEqual(result["message"], "Order Cancelled", msg="Order not cancelled" )
        self.assertEqual(response.status_code, 201)

    def test_get_all(self):
        response = self.client.get('/api/v1/parcels')
        result=json.loads(response.data.decode())
        self.assertEqual(result["message"], "Success", msg="No orders to retrieve" )
        self.assertEqual(response.status_code, 200)

    def test_get_all_by_one_user(self):
        response = self.client.get('/api/v1/parc/2')
        result=json.loads(response.data.decode())
        self.assertEqual(result["message"], "user orders", msg="User orders not found")
        self.assertEqual(response.status_code, 200)

