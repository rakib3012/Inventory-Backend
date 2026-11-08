from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_customer:int
    total_product:int
    total_invoice:int
    