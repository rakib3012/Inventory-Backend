from pydantic import BaseModel

class InvoiceItemCreate(BaseModel):
    customer_id:int
    product_id:int
    total:float
    discount:float
    vat:float
    payable:float


class InvoiceItemUpdate(BaseModel):
    customer_id:int
    proudct_id :int
    total:float
    discount:float
    vat:float
    ayable:float