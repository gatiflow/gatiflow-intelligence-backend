#!/usr/bin/env python3
"""
GatiFlow Report Generator
Transforms raw backend data into a structured intelligence report
"""

import logging
from typing import Dict, Any, List
from datetime import datetime

from talent_hunter import fetch_real_talents
from reddit_collector import collect_reddit_data

logger = logging.getLogger("GatiFlow.ReportGenerator")


class ReportGenerator:
    """
    Generates a structured intelligence report ready for frontend consumption
    """

    def __init__(self):
        self.generated_at = datetime.utcnow().isoformat() + "Z"

    def generate_market_overview(self, talents: List[Dict[str, Any]]) -> Dict[str, Any]:
        scores = [t["score"] for t in talents]

        return {
            "total_profiles_analyzed": len(talents),
            "average_score": round(sum(scores) / len(scores), 2) if scores else 0,
            "top_score": max(scores) if scores else 0,
            "generated_at": self.generated_at,
        }

    def generate_seniority_distribution(self, talents: List[Dict[str, Any]]) -> Dict[str, int]:
        distribution = {
            "leadership_90_99": 0,
            "senior_80_89": 0,
            "mid_70_79": 0,
            "junior_65_69": 0,
        }

        for talent in talents:
            score = talent["score"]

            if score >= 90:
                distribution["leadership_90_99"] += 1
            elif score >= 80:
                distribution["senior_80_89"] += 1
            elif score >= 70:
                distribution["mid_70_79"] += 1
            else:
                distribution["junior_65_69"] += 1

        return distribution

    def generate_role_distribution(self, talents: List[Dict[str, Any]]) -> Dict[str, int]:
        roles = {}

        for talent in talents:
            role = talent.get("role", "Unknown")
            roles[role] = roles.get(role, 0) + 1

        return dict(sorted(roles.items(), key=lambda x: x[1], reverse=True))

    def generate_top_talents(self, talents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(talents, key=lambda x: x["score"], reverse=True)

    def generate_insights(self, talents: List[Dict[str, Any]]) -> List[str]:
        insights = []

        avg_score = sum(t["score"] for t in talents) / len(talents) if talents else 0
        high_scorers = [t for t in talents if t["score"] >= 90]

        if avg_score >= 80:
            insights.append(
                "O mercado analisado apresenta alta maturidade técnica média."
            )
        else:
            insights.append(
                "O mercado analisado apresenta espaço significativo para desenvolvimento técnico."
            )

        if len(high_scorers) >= 3:
            insights.append(
                "Há concentração relevante de lideranças técnicas no recorte analisado."
            )
        else:
            insights.append(
                "Existe baixa concentração de lideranças técnicas, indicando possível escassez."
            )

        return insights

    def generate_report(self, limit: int = 6) -> Dict[str, Any]:
        logger.info("Generating full intelligence report...")

        talents = fetch_real_talents(limit=limit)
        reddit_trends = collect_reddit_data(limit=5)

        report = {
            "meta": {
                "product": "GatiFlow Intelligence Report",
                "version": "MVP-1.0",
                "generated_at": self.generated_at,
            },
            "market_overview": self.generate_market_overview(talents),
            "top_talents": self.generate_top_talents(talents),
            "seniority_distribution": self.generate_seniority_distribution(talents),
            "role_distribution": self.generate_role_distribution(talents),
            "strategic_insights": self.generate_insights(talents),
            "tech_trends": reddit_trends.get("trends", []),
            "methodology": {
                "data_sources": [
                    "GitHub public profiles",
                    "Reddit public communities",
                ],
                "scoring_range": "65–99",
                "ethical_notice": "All data collected from public sources with no private data usage.",
            },
        }

        logger.info("Report generation completed successfully")
        return report


def generate_report(limit: int = 6) -> Dict[str, Any]:
    generator = ReportGenerator()
    return generator.generate_report(limit=limit)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    report = generate_report(limit=6)

    print("\n" + "=" * 60)
    print("GATIFLOW — REPORT GENERATOR TEST")
    print("=" * 60)
    print(f"\nGenerated at: {report['meta']['generated_at']}")
    print(f"Profiles analyzed: {report['market_overview']['total_profiles_analyzed']}")
    print("\nTop Insights:")
    for insight in report["strategic_insights"]:
        print(f"- {insight}")
    print("\n" + "=" * 60)
