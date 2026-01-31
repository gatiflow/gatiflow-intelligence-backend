from fastapi import APIRouter, Depends, Request
from auth.api_key import get_api_key
from reports.generator import generate_report

router = APIRouter(
    prefix="/v1/intelligence",
    tags=["Intelligence"]
)


@router.post("/report")
def generate_intelligence_report(
    request: Request,
    api_key: str = Depends(get_api_key)
):
    dummy_data = {
        "github": [],
        "reddit": [],
        "hackernews": []
    }

    report = generate_report(dummy_data)

    return {
        "status": "success",
        "plan": request.state.plan,
        "data": report
    }
