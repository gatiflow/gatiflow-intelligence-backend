from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from schemas.errors import error_response


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content=error_response(
            message="Validation error",
            code="VALIDATION_ERROR",
            http_status=422,
            request_id=getattr(request.state, "request_id", None),
            details=exc.errors()
        )
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content=error_response(
            message="Internal server error",
            code="INTERNAL_ERROR",
            http_status=500,
            request_id=getattr(request.state, "request_id", None)
        )
    )
