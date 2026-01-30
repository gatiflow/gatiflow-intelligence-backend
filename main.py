from fastapi import FastAPI
from typing import Dict, Any, List
from generator import fetch_real_talents

app = FastAPI(
    title="GatiFlow Talent Intelligence API",
    description="B2B Talent Intelligence Reports based on public GitHub data",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "product": "GatiFlow",
        "status": "ok",
        "type": "Talent Intelligence API"
    }


@app.get("/report/preview")
def report_preview(limit: int = 6) -> Dict[str, Any]:
    """
    Executive preview report for B2B clients
    """
    talents = fetch_real_talents(limit=limit)

    if not talents:
        return {
            "summary": "No data available at the moment.",
            "insights": [],
            "talents": []
        }

    # --- Insights simples ---
    roles_count = {}
    high_score = []

    for t in talents:
        role = t["role"]
        roles_count[role] = roles_count.get(role, 0) + 1

        if t["score"] >= 85:
            high_score.append(t)

    insights = []

    if high_score:
        insights.append(
            f"{len(high_score)} talents apresentam score elevado (85+), indicando perfil sênior ou altamente influente."
        )

    most_common_role = max(roles_count, key=roles_count.get)
    insights.append(
        f"O papel mais recorrente entre os talentos analisados é: {most_common_role}."
    )

    insights.append(
        "Os dados indicam forte presença de profissionais com atividade consistente em projetos públicos."
    )

    # --- Resumo executivo ---
    summary = (
        f"Este relatório apresenta uma amostra qualificada de {len(talents)} "
        "profissionais de tecnologia com base em dados públicos do GitHub. "
        "O objetivo é apoiar decisões estratégicas de recrutamento, mapeamento "
        "de mercado e inteligência de talentos."
    )

    return {
        "summary": summary,
        "insights": insights,
        "talents": talents
    }
