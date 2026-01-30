#!/usr/bin/env python3
"""
GatiFlow – Main Runner

Executa a coleta de dados e gera o relatório B2B
em um único comando.
"""

import json
import logging
from datetime import datetime
from pathlib import Path

# Coletores
from devto_collector import collect_devto_data
from reddit_collector import collect_reddit_data
from stackoverflow_collector import collect_stackoverflow_data
from talent_hunter import fetch_real_talents

# Gerador de relatório
from reports.generator import generate_report


# -------------------------------------------------------------------
# Configuração básica
# -------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


# -------------------------------------------------------------------
# Execução principal
# -------------------------------------------------------------------

def main():
    logging.info("GatiFlow — starting data collection")

    raw_data = {
        "devto": collect_devto_data(limit=5).get("trends", []),
        "reddit": collect_reddit_data(limit=5).get("trends", []),
        "stackoverflow": collect_stackoverflow_data(limit=5).get("trends", []),
        "github_talents": fetch_real_talents(limit=5),
    }

    logging.info("Data collection finished")
    logging.info("Generating intelligence report")

    report = generate_report(raw_data)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"gatiflow_report_{timestamp}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    logging.info(f"Report generated successfully: {output_file}")
    logging.info("GatiFlow — execution completed")


if __name__ == "__main__":
    main()
