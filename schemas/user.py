from pydantic import BaseModel, EmailStr

class UserCrete(BaseModel):
    firstName:str
    lastName:str
    mobile:str
    email:EmailStr


class UserUpdate(BaseModel):
    user_id:str
    firstName:str
    lastName:str
    mobile:str
    email:EmailStr
    
    
class UserDelete(BaseModel):
    user_id:str
