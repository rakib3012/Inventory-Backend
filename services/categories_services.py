from sqlalchemy.orm import Session

from schemas.category import CategoryCreate, CategoryUpdate

from models.category import Category


"""
Service is a function
- DB session
- Request object/Schema -> body,params
- Model DB Query + Logic
- Return Result
"""

def category_create(db:Session,request:CategoryCreate,user_id:int):
    pass

def get_all_categories(db:Session,user_id:int):
    pass

def category_update(db:Session,request:CategoryCreate,user_id:int):
    pass

def get_category_by_id(db:Session,user_id:int, category_id:int):
    pass


def delete_category(db:Session, category_id:int, user_id:int):
    pass