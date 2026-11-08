from sqlalchemy.orm import Session
from schemas.auth import LoginRequest, RegistrationReques, SendOtpRequest,SetPasswordRequest,VerifyOtpRequest

from models.user import User


"""
Service is a function
- DB session
- Request object/Schema -> body,params
- Model DB Query + Logic
- Return Result
"""


def login_user(db:Session,request:LoginRequest):
    pass


def register_user(db:Session,request:RegistrationReques):
    pass

def send_otp(db:Session,request:SendOtpRequest):
    pass

def set_password(db:Session,request:SetPasswordRequest):
    pass