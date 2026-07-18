from fastapi import FastAPI

from app.core.config import settings
from app.routers.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "status": "online",
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
    }