from typing import List
from pydantic import BaseModel


class MarketTrend(BaseModel):
    trend: str
    growth: str
    source: str


class TalentSignal(BaseModel):
    skill: str
    demand: str
    source: str


class HiringSignal(BaseModel):
    role: str
    openings: int
    region: str


class IntelligenceReport(BaseModel):
    market_trends: List[MarketTrend]
    talent_signals: List[TalentSignal]
    hiring_signals: List[HiringSignal]


def intelligence_report_schema(
    market_trends,
    talent_signals,
    hiring_signals
):
    return IntelligenceReport(
        market_trends=market_trends,
        talent_signals=talent_signals,
        hiring_signals=hiring_signals
    )
