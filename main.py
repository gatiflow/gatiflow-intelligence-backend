from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routes.v1.intelligence import router as intelligence_v1_router
from routes.v1.admin import router as admin_v1_router

from middleware.request_id import RequestIDMiddleware
from middleware.rate_limit_headers import RateLimitHeadersMiddleware
from middleware.error_handler import (
    validation_exception_handler,
    generic_exception_handler
)

app = FastAPI(
    title="GatiFlow Intelligence API",
    version="1.0.0",
    description="Ethical, compliant and audit-ready market intelligence API"
)

# ===============================
# Middlewares
# ===============================
app.add_middleware(RequestIDMiddleware)
app.add_middleware(RateLimitHeadersMiddleware)

# ===============================
# Exception Handlers
# ===============================
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# ===============================
# Root Health Check
# ===============================
@app.get("/", tags=["Health"])
def root():
    return {
        "product": "GatiFlow Intelligence API",
        "status": "ok",
        "authentication": "API Key required",
        "version": app.version
    }

# ===============================
# Routers
# ===============================
app.include_router(
    intelligence_v1_router,
    prefix="/v1/intelligence",
    tags=["Intelligence"]
)

app.include_router(
    admin_v1_router,
    prefix="/v1/admin",
    tags=["Admin"]
)
