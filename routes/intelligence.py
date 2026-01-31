from fastapi import APIRouter, Depends
from auth.api_key import verify_api_key
from schemas.intelligence_report import intelligence_report_schema

router = APIRouter(prefix="/intelligence", tags=["Intelligence"])


@router.get("/report")
def get_intelligence_report(auth=Depends(verify_api_key)):
    return intelligence_report_schema(
        market_trends=[
            {"trend": "AI Adoption", "growth": "+42%", "source": "GitHub"}
        ],
        talent_signals=[
            {"skill": "Python", "demand": "High", "source": "StackOverflow"}
        ],
        hiring_signals=[
            {"role": "Data Engineer", "openings": 1280, "region": "Global"}
        ]
    )
