from fastapi import APIRouter


router = APIRouter()



@router.get("/products")
async def products():
    return{"msg":"all products"}

@router.get("/product/{product_id}")
async def single_product():
    return{"msg":"one product"}

@router.post("/add-product")
async def add_product():
    return{"msg":"product added"}


@router.put("/update-product/{product_id}")
async def update_product():
    return{"msg":"product updated"}


@router.delete("/delete-product/{product_id}")
async def delete_product():
    return{"msg":"delete successfull"}


