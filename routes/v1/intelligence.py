from fastapi import APIRouter, Depends, Query
from auth.dependencies import require_api_key
from reports.generator import generate_report

router = APIRouter(
    prefix="/v1/intelligence",
    tags=["Intelligence"]
)


@router.get(
    "/report",
    summary="Get B2B Market & Talent Intelligence Report",
    description=(
        "Returns a consolidated intelligence report generated exclusively "
        "from public technical signals. Access is protected by API Key."
    )
)
def get_intelligence_report(
    limit: int = Query(
        default=6,
        ge=1,
        le=50,
        description="Maximum number of talent profiles analyzed in the report"
    ),
    api_key: str = Depends(require_api_key)
):
    """
    B2B Intelligence Report Endpoint

    - Requires valid API Key
    - Uses only public, non-personal data
    - Returns audit-ready intelligence JSON
    """
    return generate_report(limit=limit)
