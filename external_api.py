from pymongo import MongoClient
from datetime import datetime
import random

class ExternalAPI:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="moodscale_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def create_client(self, name, email, phone):
        new_id = self.db.clients.estimated_document_count() + 1
        self.db.clients.insert_one({
            "_id": new_id,
            "name": name,
            "email": email,
            "phone": phone,
            "enrolled_services": []
        })
        return f"✅ Client {name} added with ID {new_id}"

    def create_order(self, client_id, course_id):
        order_id = f"ORD{random.randint(1000, 9999)}"
        self.db.orders.insert_one({
            "_id": order_id,
            "client_id": client_id,
            "course_id": course_id,
            "status": "pending",
            "created_at": str(datetime.now())
        })
        return f"🛒 Order {order_id} created for client {client_id} and course {course_id}"
