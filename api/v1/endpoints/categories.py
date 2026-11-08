from fastapi import APIRouter


router = APIRouter()



@router.get("/categories")
async def categories():
    return{"msg":"all categories"}

@router.get("/category/{category_id}")
async def single_category():
    return{"msg":"one category"}

@router.post("/add-category")
async def add_category():
    return{"msg":"category added"}


@router.put("/update-category/{category_id}")
async def update_category():
    return{"msg":"category updated"}


@router.delete("/delete-category/{category_id}")
async def delete_category():
    return{"msg":"delete successfull"}


