 

from fastapi import APIRouter


router = APIRouter()

@router.get("/dashboard")
async def dashboard():
    return{"msg":"all dashboard"}

@router.get("/stats")
async def stats():
    return{"msg":"stats"}


@router.get("/recent-activities")
async def recent_activities():
    return{"msg":"all activities"}


