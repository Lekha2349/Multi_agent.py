from mongo_tools import MongoDBTool

class DashboardAgent:
    def __init__(self):
        self.db_tool = MongoDBTool()

    def handle_query(self, query):
        query = query.lower()

        if "revenue" in query:
            return f"💰 Total Revenue: ₹{self.db_tool.total_revenue()}"

        elif "outstanding" in query:
            return f"💸 Outstanding Payments: ₹{self.db_tool.outstanding_payments()}"

        elif "inactive clients" in query:
            return f"🙍 Inactive Clients: {self.db_tool.inactive_clients()}"

        elif "active clients" in query:
            return f"🙂 Active Clients: {self.db_tool.active_clients()}"

        else:
            return "📊 Sorry, I couldn't process that analytics question."
