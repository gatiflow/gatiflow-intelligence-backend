"""
GatiFlow Intelligence
Report Generator

Gera o relatório B2B consolidado a partir dos dados brutos
coletados pelo backend.

Saída: JSON estruturado e pronto para consumo (frontend / cliente)
"""

from datetime import datetime
from typing import Dict, List, Any


class ReportGenerator:
    def __init__(self, raw_data: Dict[str, Any]):
        """
        raw_data esperado (exemplo):
        {
            "hackernews": [...],
            "reddit": [...],
            "devto": [...],
            "stackoverflow": [...],
            "github": [...]
        }
        """
        self.raw_data = raw_data
        self.generated_at = datetime.utcnow().isoformat()

    def generate(self) -> Dict[str, Any]:
        """
        Gera o relatório final consolidado
        """
        return {
            "metadata": self._build_metadata(),
            "executive_summary": self._build_executive_summary(),
            "market_signals": self._build_market_signals(),
            "technology_trends": self._build_technology_trends(),
            "opportunities": self._build_opportunities(),
            "risks": self._build_risks(),
            "raw_sources_count": self._build_sources_count()
        }

    # ------------------------------------------------------------------
    # Seções do relatório
    # ------------------------------------------------------------------

    def _build_metadata(self) -> Dict[str, Any]:
        return {
            "product": "GatiFlow Intelligence",
            "report_type": "Tech & Market Signals",
            "generated_at": self.generated_at
        }

    def _build_executive_summary(self) -> Dict[str, Any]:
        """
        Resumo executivo simples e objetivo (B2B)
        """
        total_items = sum(len(v) for v in self.raw_data.values() if isinstance(v, list))

        return {
            "overview": (
                "Este relatório consolida sinais técnicos e de mercado "
                "extraídos de comunidades de desenvolvedores e tecnologia."
            ),
            "total_signals_analyzed": total_items,
            "key_takeaway": (
                "Há concentração de discussões em ferramentas, IA aplicada "
                "e automação, indicando oportunidades de produto e consultoria."
            )
        }

    def _build_market_signals(self) -> List[Dict[str, Any]]:
        """
        Sinais de mercado (problemas, dores, demandas)
        """
        signals = []

        for source, items in self.raw_data.items():
            for item in items[:5]:  # limita para manter relatório enxuto
                signals.append({
                    "source": source,
                    "title": item.get("title"),
                    "signal_type": "market_demand",
                    "confidence": "medium"
                })

        return signals

    def _build_technology_trends(self) -> List[Dict[str, Any]]:
        """
        Tendências tecnológicas detectadas
        """
        trends = []

        for source, items in self.raw_data.items():
            for item in items[:5]:
                trends.append({
                    "source": source,
                    "topic": item.get("tags") or item.get("keywords"),
                    "trend_strength": "emerging"
                })

        return trends

    def _build_opportunities(self) -> List[Dict[str, Any]]:
        """
        Oportunidades claras para empresas / startups
        """
        return [
            {
                "opportunity": "Ferramentas internas de automação",
                "description": (
                    "Alta recorrência de discussões sobre produtividade e IA "
                    "indica demanda por soluções customizadas."
                ),
                "target": "Startups e empresas médias"
            },
            {
                "opportunity": "Consultoria em adoção de IA",
                "description": (
                    "Muitos sinais indicam interesse, mas falta de clareza "
                    "sobre implementação prática."
                ),
                "target": "Times de produto e engenharia"
            }
        ]

    def _build_risks(self) -> List[Dict[str, Any]]:
        """
        Riscos percebidos no mercado
        """
        return [
            {
                "risk": "Hype tecnológico",
                "description": (
                    "Algumas tendências podem não se sustentar no médio prazo."
                )
            },
            {
                "risk": "Saturação de ferramentas",
                "description": (
                    "Mercado competitivo exige diferenciação clara."
                )
            }
        ]

    def _build_sources_count(self) -> Dict[str, int]:
        """
        Contagem de itens analisados por fonte
        """
        return {
            source: len(items)
            for source, items in self.raw_data.items()
            if isinstance(items, list)
        }


# ----------------------------------------------------------------------
# Função utilitária (facilita uso via script ou API)
# ----------------------------------------------------------------------

def generate_report(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    generator = ReportGenerator(raw_data)
    return generator.generate()
