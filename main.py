#!/usr/bin/env python3
"""
GatiFlow Executive Intelligence API
B2B Market & Talent Intelligence Report Generator
"""

from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from generator import generate_executive_report

app = FastAPI(
    title="GatiFlow Executive Intelligence API",
    description="B2B Market & Talent Intelligence Reports based on ethical public data",
    version="1.0.0"
)

# CORS (libera frontend, PDF generators, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "product": "GatiFlow Executive Intelligence API",
        "status": "running",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/report")
def get_executive_report():
    """
    Generates the full executive B2B intelligence report.
    This is the main commercial endpoint.
    """
    report = generate_executive_report()
    return report
