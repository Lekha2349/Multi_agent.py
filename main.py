from fastapi import FastAPI
from pydantic import BaseModel
from support_agent import SupportAgent
from dashboard_agent import DashboardAgent

app = FastAPI()
support = SupportAgent()
dashboard = DashboardAgent()

class QueryRequest(BaseModel):
    query: str

@app.post("/support")
def support_query(req: QueryRequest):
    return {"response": support.handle_query(req.query)}

@app.post("/dashboard")
def dashboard_query(req: QueryRequest):
    return {"response": dashboard.handle_query(req.query)}
