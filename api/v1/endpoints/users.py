from fastapi import APIRouter


router = APIRouter()



@router.get("/users")
async def users():
    return{"msg":"all users"}

@router.get("/user/{user_id}")
async def single_user():
    return{"msg":"one user"}

@router.post("/add-user")
async def add_user():
    return{"msg":"user added"}


@router.put("/update-user/{user_id}")
async def update_user():
    return{"msg":"user updated"}


@router.delete("/delete-user/{user_id}")
async def delete_user():
    return{"msg":"delete successfull"}


