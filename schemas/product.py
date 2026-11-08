from pydantic import BaseModel,EmailStr


class ProductCreate(BaseModel):
    title:str
    qty:int
    price:int



class ProductUpdate(BaseModel):
    product_id:str
    product_price:int
    product_qty:int