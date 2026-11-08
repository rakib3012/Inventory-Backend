from fastapi import APIRouter



router = APIRouter()



@router.post("/login")
async def login():
    return{"message":"login success"}


@router.post("/registration")
async def registration():
    return{
        "message":"registration successfull"
    }


@router.post("/send-otp")
async def send_otp():
    return{"msg":"otp send"}


@router.post("/verify-otp")
async def verify_otp():
    return{"msg":"otp verified"}


@router.post("/setpass")
async def setpass():
    return{"msg":"password rest successfully"}

