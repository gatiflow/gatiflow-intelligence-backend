"""
GatiFlow Intelligence
Report Generator

Gera relatórios B2B consolidados a partir de sinais técnicos públicos.
Este é o CORE vendável do produto.
"""

from datetime import datetime, timezone
from typing import Dict, Any, List
import logging

# -------------------------------------------------
# Logging
# -------------------------------------------------

logger = logging.getLogger("GatiFlow.ReportGenerator")

# -------------------------------------------------
# Mock / Data Providers (substituíveis futuramente)
# -------------------------------------------------

def fetch_real_talents(limit: int = 6) -> List[Dict[str, Any]]:
    """
    Simula coleta de talentos técnicos (GitHub, fóruns públicos, etc).
    Nenhum dado pessoal ou privado é utilizado.
    """
    return [
        {
            "username": f"dev_{i}",
            "role": "Backend Engineer" if i % 2 == 0 else "Data Engineer",
            "score": 70 + i * 4
        }
        for i in range(1, limit + 1)
    ]


def collect_market_trends(limit: int = 5) -> List[Dict[str, Any]]:
    """
    Simula detecção de tendências de mercado a partir de fontes públicas.
    """
    trends = [
        {"topic": "AI Automation", "signal_strength": "high"},
        {"topic": "Data Engineering", "signal_strength": "medium"},
        {"topic": "Cloud Cost Optimization", "signal_strength": "medium"},
        {"topic": "Internal Developer Platforms", "signal_strength": "emerging"},
        {"topic": "MLOps Tooling", "signal_strength": "emerging"},
    ]
    return trends[:limit]

# -------------------------------------------------
# Report Generator
# -------------------------------------------------

def generate_report(limit: int = 6) -> Dict[str, Any]:
    """
    Gera um relatório de inteligência pronto para:
    - API REST
    - Consumo por frontend
    - Entrega B2B
    - Auditoria e compliance
    """

    generated_at = datetime.now(timezone.utc).isoformat()

    talents = fetch_real_talents(limit=limit)
    market_trends = collect_market_trends()

    scores = [t["score"] for t in talents]
    average_score = round(sum(scores) / len(scores), 2) if scores else 0
    top_score = max(scores) if scores else 0

    # -------------------------------------------------
    # Strategic Insights
    # -------------------------------------------------

    strategic_insights: List[str] = []

    if average_score >= 80:
        strategic_insights.append(
            "O mercado analisado apresenta alta maturidade técnica média."
        )
    else:
        strategic_insights.append(
            "O mercado analisado indica espaço relevante para capacitação técnica."
        )

    leadership_count = len([t for t in talents if t["score"] >= 90])
    if leadership_count >= 2:
        strategic_insights.append(
            "Há concentração relevante de lideranças técnicas no recorte analisado."
        )
    else:
        strategic_insights.append(
            "Baixa densidade de lideranças técnicas pode indicar escassez futura."
        )

    # -------------------------------------------------
    # Final Report (Contrato B2B)
    # -------------------------------------------------

    report: Dict[str, Any] = {
        "metadata": {
            "product": "GatiFlow Intelligence",
            "report_type": "Market & Talent Intelligence",
            "version": "1.0",
            "generated_at": generated_at
        },
        "overview": {
            "total_profiles_analyzed": len(talents),
            "average_score": average_score,
            "top_score": top_score
        },
        "talent_signals": sorted(
            talents,
            key=lambda x: x["score"],
            reverse=True
        ),
        "market_trends": market_trends,
        "strategic_insights": strategic_insights,
        "methodology": {
            "data_sources": [
                "Public GitHub activity",
                "Public technical discussions"
            ],
            "scoring_range": "65–99",
            "ethical_notice": (
                "All insights are derived exclusively from public sources. "
                "No private, personal, or sensitive data is collected or processed."
            )
        }
    }

    logger.info("Intelligence report generated successfully")
    return report
