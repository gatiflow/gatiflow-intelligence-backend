from fastapi import FastAPI
from routes.intelligence import router as intelligence_router

app = FastAPI(
    title="GatiFlow Intelligence API",
    description="Compliant Market, Talent and Hiring Intelligence",
    version="1.0.0"
)

app.include_router(intelligence_router)


@app.get("/")
def root():
    return {
        "product": "GatiFlow Intelligence API",
        "status": "running",
        "compliance": ["GDPR", "LGPD"]
    }
