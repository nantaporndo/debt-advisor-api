import os

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])

class HealthResponse(BaseModel):
    status: str
    version: str

@router.get("/health", response_model=HealthResponse)
def health()-> HealthResponse:
    return HealthResponse(status="ok",version=os.getenv("APP_VERSION","dev"))