from mongo_tools import MongoDBTool
from external_api import ExternalAPI

class SupportAgent:
    def __init__(self):
        self.db_tool = MongoDBTool()
        self.api = ExternalAPI()

    def handle_query(self, query):
        query = query.lower()

        if "class" in query and "available" in query:
            classes = self.db_tool.list_classes()
            return [f"{cls['date']} - {cls['instructor']}" for cls in classes]

        elif "has order" in query and "been paid" in query:
            order_id = query.split("#")[-1].strip()
            payments = self.db_tool.get_payments(order_id)
            if not payments:
                return "No payment found."
            return "✅ Paid" if payments[0]["paid"] else "❌ Not paid"

        elif "create an order" in query:
            if "yoga" in query:
                course_id = 101
            elif "pilates" in query:
                course_id = 102
            else:
                return "❌ Course not found."

            if "priya" in query:
                client_id = 1
            elif "ravi" in query:
                client_id = 2
            else:
                return "❌ Client not found."

            return self.api.create_order(client_id, course_id)

        else:
            return "🤖 Sorry, I didn't understand that support request."
