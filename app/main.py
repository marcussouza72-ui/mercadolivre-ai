from fastapi import FastAPI

from app.core.config import settings
from app.exceptions.handlers import register_exception_handlers
from app.routers.auth import router as auth_router
from app.routers.health import router as health_router
from app.api.v1.routers.mercadolivre import router as mercadolivre_router

app = FastAPI(
    title="MERCADO LIVRE AI - TESTE 999",
    debug=settings.DEBUG,
)

register_exception_handlers(app)

# Routers
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(mercadolivre_router)


@app.get(
    "/",
    summary="Status da aplicação",
    tags=["System"],
)
def root():
    return {
        "status": "online",
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
    }