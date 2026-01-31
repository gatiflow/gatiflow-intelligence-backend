from fastapi import FastAPI
from routes.v1.intelligence import router as intelligence_v1_router

app = FastAPI(
    title="GatiFlow Intelligence API",
    description="Enterprise-grade market and talent intelligence from public data",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "product": "GatiFlow",
        "status": "ok",
        "type": "Intelligence API"
    }


app.include_router(intelligence_v1_router)
