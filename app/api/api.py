from fastapi import APIRouter

from app.api.handlers import ping, profile

api_router = APIRouter()

api_router.include_router(ping.router, prefix="/ping", tags=["ping"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
