from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import create_tables
from contextlib import asynccontextmanager
from api.v1.api import router as api_router
import uvicorn

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("starting up application")
    create_tables()
    print("database table create successfully")
    yield
    print("shutting down application...")
    
    
app = FastAPI(
    title="inventory api",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    api_router,
    prefix="/api/v1"
)

app.get("/")
async def root():
    return{"msg":"hellow inventory"}

app.get("/health")
async def health():
    return{"msg":"app is healthy"}

if __name__ == "__main__":
     uvicorn.run(
         app,
         host="0.0.0.0",
         port=8000,
         reload=True
     )
    