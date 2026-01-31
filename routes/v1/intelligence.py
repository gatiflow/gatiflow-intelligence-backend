from fastapi import APIRouter, Depends
from auth.api_key import verify_api_key
from schemas.intelligence_report import intelligence_report_schema
from schemas.response import response_envelope

router = APIRouter(
    prefix="/v1/intelligence",
    tags=["Intelligence v1"],
    dependencies=[Depends(verify_api_key)]
)


@router.get("/report")
def get_intelligence_report():
    market_trends = [
        {"trend": "AI Adoption", "growth": "+42%", "source": "GitHub"},
        {"trend": "Cloud Native", "growth": "+28%", "source": "CNCF"}
    ]

    talent_signals = [
        {"skill": "Python", "demand": "High", "source": "GitHub"},
        {"skill": "Data Engineering", "demand": "Rising", "source": "StackOverflow"}
    ]

    hiring_signals = [
        {"role": "AI Engineer", "openings": 1200, "region": "Global"},
        {"role": "Data Engineer", "openings": 860, "region": "North America"}
    ]

    report = intelligence_report_schema(
        market_trends=market_trends,
        talent_signals=talent_signals,
        hiring_signals=hiring_signals
    )

    return response_envelope(
        data=report.dict(),
        message="Intelligence report generated successfully"
    )
