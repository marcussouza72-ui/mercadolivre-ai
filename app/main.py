from fastapi import FastAPI

app = FastAPI(
    title="Mercado Livre AI Integration",
    description="API para integração com Mercado Livre e IA",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "application": "Mercado Livre AI Integration",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
