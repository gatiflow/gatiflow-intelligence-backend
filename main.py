from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import asyncio
import json
import logging

from report_generator import generate_report

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GatiFlow.API")

app = FastAPI(
    title="GatiFlow Intelligence API",
    description="B2B Market & Talent Intelligence based on public technical signals",
    version="1.0.0"
)

# -------------------------------------------------
# CORS (frontend dashboard)
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajustar em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Healthcheck
# -------------------------------------------------
@app.get("/")
def healthcheck() -> Dict[str, Any]:
    return {
        "product": "GatiFlow Intelligence",
        "status": "ok",
        "type": "B2B Intelligence API"
    }

# -------------------------------------------------
# Intelligence Report Endpoint
# -------------------------------------------------
@app.get("/intelligence/report")
def intelligence_report(limit: int = 6) -> Dict[str, Any]:
    """
    Gera relatório B2B consolidado (on-demand)
    """
    logger.info("Generating intelligence report via API")
    return generate_report(limit=limit)

# -------------------------------------------------
# WebSocket Manager
# -------------------------------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info("WebSocket client connected")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info("WebSocket client disconnected")

    async def broadcast(self, message: Dict[str, Any]):
        for connection in self.active_connections:
            await connection.send_text(json.dumps(message))


manager = ConnectionManager()

# -------------------------------------------------
# WebSocket Endpoint
# -------------------------------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # mantém conexão viva
            await asyncio.sleep(10)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# -------------------------------------------------
# Background Task: Push Intelligence Updates
# -------------------------------------------------
async def intelligence_push_loop():
    while True:
        try:
            report = generate_report(limit=6)
            payload = {
                "event": "update",
                "generated_at": report["metadata"]["generated_at"],
                "report": report
            }
            await manager.broadcast(payload)
            logger.info("Pushed intelligence update to WebSocket clients")
        except Exception as e:
            logger.error(f"WebSocket push error: {e}")

        await asyncio.sleep(60)  # intervalo de atualização


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(intelligence_push_loop())
