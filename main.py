#!/usr/bin/env python3
"""
GatiFlow API
Main entrypoint for report generation
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import time
import logging

from generator import generate_report

# ------------------------------------------------------------------
# App setup
# ------------------------------------------------------------------

app = FastAPI(
    title="GatiFlow Intelligence API",
    description="B2B Tech Intelligence & Talent Signals",
    version="0.1.0"
)

# Allow frontend access later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("GatiFlow.API")

# ------------------------------------------------------------------
# Health check
# ------------------------------------------------------------------

@app.get("/")
def health_check() -> Dict[str, Any]:
    return {
        "status": "ok",
        "service": "GatiFlow API",
        "timestamp": time.time()
    }

# ------------------------------------------------------------------
# Core endpoint
# ------------------------------------------------------------------

@app.post("/generate-report")
def generate_intelligence_report() -> Dict[str, Any]:
    """
    Generates a full intelligence report combining:
    - Reddit trends
    - StackOverflow insights
    - GitHub talent signals
    """

    logger.info("Generating intelligence report")

    try:
        report = generate_report()

        return {
            "success": True,
            "generated_at": time.time(),
            "report": report
        }

    except Exception as e:
        logger.error(f"Report generation failed: {e}")

        return {
            "success": False,
            "error": str(e)
        }
