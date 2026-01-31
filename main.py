from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routes.v1.intelligence import router as intelligence_v1_router
from middleware.request_id import RequestIDMiddleware
from middleware.error_handler import (
    validation_exception_handler,
    generic_exception_handler
)

app = FastAPI(
    title="GatiFlow Intelligence API",
    description="Enterprise-grade market and talent intelligence from public data",
    version="1.0.0"
)

# ----------------------------
# Middleware
# ----------------------------
app.add_middleware(RequestIDMiddleware)

# ----------------------------
# Exception handlers
# ----------------------------
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# ----------------------------
# Routes
# ----------------------------
@app.get("/")
def root():
    return {
        "product": "GatiFlow",
        "status": "ok",
        "type": "Intelligence API"
    }


app.include_router(intelligence_v1_router)
