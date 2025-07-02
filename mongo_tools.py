from pymongo import MongoClient

class MongoDBTool:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="moodscale_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def find_client(self, query):
        return list(self.db.clients.find({
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"email": {"$regex": query, "$options": "i"}},
                {"phone": {"$regex": query}}
            ]
        }))

    def get_orders(self, client_id=None, status=None):
        query = {}
        if client_id:
            query["client_id"] = client_id
        if status:
            query["status"] = status
        return list(self.db.orders.find(query))

    def get_payments(self, order_id):
        return list(self.db.payments.find({"order_id": order_id}))

    def list_classes(self, instructor=None):
        query = {}
        if instructor:
            query["instructor"] = instructor
        return list(self.db.classes.find(query))

    def total_revenue(self):
        return sum([p["amount"] for p in self.db.payments.find({"paid": True})])

    def outstanding_payments(self):
        return sum([p["amount"] for p in self.db.payments.find({"paid": False})])

    def active_clients(self):
        return self.db.clients.count_documents({"enrolled_services": {"$ne": []}})

    def inactive_clients(self):
        return self.db.clients.count_documents({"enrolled_services": []})
