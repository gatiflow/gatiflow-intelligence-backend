from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routes.v1.intelligence import router as intelligence_v1_router
from middleware.request_id import RequestIDMiddleware
from middleware.rate_limit_headers import RateLimitHeadersMiddleware
from middleware.error_handler import (
    validation_exception_handler,
    generic_exception_handler
)

app = FastAPI(
    title="GatiFlow Intelligence API",
    version="1.0.0"
)

app.add_middleware(RequestIDMiddleware)
app.add_middleware(RateLimitHeadersMiddleware)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/")
def root():
    return {
        "product": "GatiFlow",
        "status": "ok",
        "access": "API Key required"
    }

app.include_router(intelligence_v1_router)
