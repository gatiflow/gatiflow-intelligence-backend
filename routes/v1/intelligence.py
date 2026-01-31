from fastapi import APIRouter, Depends

from auth.dependencies import require_api_key
from reports.generator import generate_report

router = APIRouter(
    prefix="/intelligence",
    tags=["Intelligence"]
)


@router.get("/report")
def get_intelligence_report(api_key: str = Depends(require_api_key)):
    """
    Returns a consolidated B2B intelligence report.
    Access protected by API Key.
    """
    return generate_report()
