from fastapi import APIRouter


router = APIRouter()



@router.get("/invoices")
async def invoices():
    return{"msg":"all invoices"}

@router.get("/invoice/{invoice_id}")
async def single_invoice():
    return{"msg":"one invoice"}

@router.post("/add-invoice")
async def add_invoice():
    return{"msg":"invoice added"}


@router.put("/update-invoice/{invoice_id}")
async def update_invoice():
    return{"msg":"invoice updated"}


@router.delete("/delete-invoice/{invoice_id}")
async def delete_invoice():
    return{"msg":"delete successfull"}


