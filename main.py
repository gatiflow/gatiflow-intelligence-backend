from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict, Any, List
from generator import fetch_real_talents
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="GatiFlow Talent Intelligence API",
    description="B2B Talent Intelligence Reports based on public GitHub data",
    version="0.1.0"
)

# -------------------------------
# CORS para frontend
# -------------------------------
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# -------------------------------
# ROOT ENDPOINT
# -------------------------------
@app.get("/")
def root():
    return {
        "product": "GatiFlow",
        "status": "ok",
        "type": "Talent Intelligence API"
    }

# -------------------------------
# REPORT PREVIEW
# -------------------------------
@app.get("/report/preview")
def report_preview(limit: int = 6) -> Dict[str, Any]:
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

# -------------------------------
# WEBSOCKET MANAGER
# -------------------------------
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: Dict[str, Any]):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

# -------------------------------
# WEBSOCKET ENDPOINT
# -------------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Aguarda mensagens do cliente (não usado aqui, mas mantém conexão)
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# -------------------------------
# FUNÇÃO PARA BROADCAST DE NOVOS DADOS
# -------------------------------
import asyncio

async def notify_new_talents():
    """
    Simula envio de dados atualizados para todos os clientes WebSocket
    """
    while True:
        await asyncio.sleep(10)  # intervalos de 10s
        talents = fetch_real_talents(limit=6)
        data = {
            "event": "update",
            "talents": talents
        }
        if talents:
            await manager.broadcast(data)
