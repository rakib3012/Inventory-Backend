from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
   email:EmailStr
   password:str


class RegistrationReques(BaseModel):
    firstName:str
    lastName:str
    email:EmailStr
    mobile:str
    password: str



class SendOtpRequest(BaseModel):
    emai:EmailStr

class VerifyOtpRequest(BaseModel):
    email:EmailStr
    otp:str

class SetPasswordRequest(BaseModel):
    emai:EmailStr
    password:str
    otp:str