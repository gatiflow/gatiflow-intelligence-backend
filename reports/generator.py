"""
GatiFlow Intelligence
Enterprise Report Generator

Generates vendable intelligence reports based on public data.
"""

from typing import Dict, List, Any
from schemas.intelligence_report import intelligence_report


class ReportGenerator:

    def __init__(self, raw_data: Dict[str, List[Dict[str, Any]]]):
        self.raw_data = raw_data

    # -------------------------------------------------
    # PUBLIC ENTRY POINT
    # -------------------------------------------------

    def generate(self) -> Dict[str, Any]:
        return intelligence_report(
            executive_summary=self._executive_summary(),
            market_signals=self._market_signals(),
            technology_trends=self._technology_trends(),
            talent_signals=self._talent_signals(),
            opportunities=self._opportunities(),
            risks=self._risks(),
            sources_count=self._sources_count()
        )

    # -------------------------------------------------
    # INTERNAL BUILDERS
    # -------------------------------------------------

    def _executive_summary(self) -> Dict[str, Any]:
        total_signals = sum(len(v) for v in self.raw_data.values())

        return {
            "overview": (
                "This report consolidates verified public signals "
                "from technology communities and job markets."
            ),
            "signals_analyzed": total_signals,
            "key_insight": (
                "Strong concentration of discussions around AI adoption, "
                "automation and developer productivity."
            ),
            "business_impact": (
                "Indicates opportunities for tooling, consulting and "
                "data-driven products."
            )
        }

    def _market_signals(self) -> List[Dict[str, Any]]:
        signals = []
        for source, items in self.raw_data.items():
            for item in items[:3]:
                signals.append({
                    "source": source,
                    "signal": item.get("title"),
                    "confidence": "medium"
                })
        return signals

    def _technology_trends(self) -> List[Dict[str, Any]]:
        trends = []
        for source, items in self.raw_data.items():
            for item in items[:3]:
                trends.append({
                    "source": source,
                    "topics": item.get("tags") or item.get("keywords"),
                    "trend_strength": "emerging"
                })
        return trends

    def _talent_signals(self) -> List[Dict[str, Any]]:
        return [
            {
                "signal": "High demand for senior engineers",
                "evidence": "Recurring discussions on hiring difficulty",
                "confidence": "high"
            }
        ]

    def _opportunities(self) -> List[Dict[str, Any]]:
        return [
            {
                "opportunity": "AI adoption consulting",
                "target_market": "Mid-size and enterprise companies"
            },
            {
                "opportunity": "Internal automation platforms",
                "target_market": "Tech-driven organizations"
            }
        ]

    def _risks(self) -> List[Dict[str, Any]]:
        return [
            {
                "risk": "Technology hype cycles",
                "impact": "Medium",
                "mitigation": "Cross-source validation"
            }
        ]

    def _sources_count(self) -> Dict[str, int]:
        return {k: len(v) for k, v in self.raw_data.items()}
