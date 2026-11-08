from fastapi import APIRouter


router = APIRouter()



@router.get("/customers")
async def customers():
    return{"msg":"all customers"}

@router.get("/customer/{customer_id}")
async def single_customer():
    return{"msg":"one customer"}

@router.post("/add-customer")
async def add_customer():
    return{"msg":"customer added"}


@router.put("/update-customer/{customer_id}")
async def update_customer():
    return{"msg":"customer updated"}


@router.delete("/delete-customer/{customer_id}")
async def delete_customer():
    return{"msg":"delete successfull"}


