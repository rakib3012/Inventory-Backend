from sqlalchemy.orm import Session
from schemas.customer import CustomerCreate,CustomerUpdate
from models.customer import Customer


"""
Service is a function
- DB session
- Request object/Schema -> body,params
- Model DB Query + Logic
- Return Result
"""


def create_customer(db:Session,request:CustomerCreate,user_id:int):
    pass

def update_customer(db:Session,request:CustomerUpdate,user_id:int):
    pass
