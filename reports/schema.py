"""
GatiFlow Intelligence Report Schema
Defines the structure of vendable B2B intelligence reports
"""

from typing import Dict, List, Any
from datetime import datetime, timezone


def base_metadata() -> Dict[str, Any]:
    """Standard metadata for all intelligence reports"""
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "product": "GatiFlow Intelligence",
        "report_version": "1.0",
        "confidentiality": "B2B Internal / Client Use"
    }


def intelligence_report_schema(
    market_trends: List[Dict[str, Any]],
    talent_signals: List[Dict[str, Any]],
    hiring_signals: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Standard vendable intelligence report schema
    """
    return {
        "metadata": base_metadata(),
        "sections": {
            "executive_summary": {
                "title": "Market & Talent Intelligence Overview",
                "summary": "Strategic signals extracted from public technology ecosystems."
            },
            "market_trends": {
                "title": "Technology & Market Trends",
                "data": market_trends
            },
            "talent_signals": {
                "title": "Talent Intelligence Signals",
                "data": talent_signals
            },
            "hiring_signals": {
                "title": "Hiring & Opportunity Signals",
                "data": hiring_signals
            }
        }
    }
