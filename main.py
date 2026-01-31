from fastapi import FastAPI
from report_generator import ReportGenerator

app = FastAPI(
    title="GatiFlow Intelligence API",
    description="Ethical Market & Talent Intelligence based on public data",
    version="1.0.0"
)


@app.get("/")
def healthcheck():
    return {
        "status": "ok",
        "product": "GatiFlow Intelligence"
    }


@app.post("/intelligence/report")
def generate_intelligence_report(raw_data: dict):
    generator = ReportGenerator(raw_data)
    return generator.generate()
