from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "debug": settings.DEBUG,
    }