"""
GatiFlow Intelligence
Official B2B Intelligence Report Schema

This schema defines the commercial contract exposed to clients.
Stable, versioned and audit-ready.
"""

from typing import Dict, List, Any
from datetime import datetime, timezone


def metadata_block(report_type: str) -> Dict[str, Any]:
    return {
        "product": "GatiFlow Intelligence",
        "report_type": report_type,
        "schema_version": "1.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "compliance": {
            "gdpr": True,
            "lgpd": True,
            "personal_data": False,
            "sources": "public_only"
        }
    }


def intelligence_report(
    executive_summary: Dict[str, Any],
    market_signals: List[Dict[str, Any]],
    technology_trends: List[Dict[str, Any]],
    talent_signals: List[Dict[str, Any]],
    opportunities: List[Dict[str, Any]],
    risks: List[Dict[str, Any]],
    sources_count: Dict[str, int]
) -> Dict[str, Any]:

    return {
        "metadata": metadata_block("Market & Talent Intelligence"),
        "executive_summary": executive_summary,
        "market_signals": market_signals,
        "technology_trends": technology_trends,
        "talent_signals": talent_signals,
        "opportunities": opportunities,
        "risks": risks,
        "sources_count": sources_count
    }
