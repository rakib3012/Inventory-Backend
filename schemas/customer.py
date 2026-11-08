from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name:str
    mobile:str
    email:EmailStr


class CustomerUpdate(BaseModel):
    name:str
    email:EmailStr
    mobile:str


