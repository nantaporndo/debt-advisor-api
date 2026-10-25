from fastapi import APIRouter

from app.api import debts

api_router = APIRouter()
api_router.include_router(debts.router)
