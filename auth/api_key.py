"""
GatiFlow Intelligence
API Key Authentication Layer

Autenticação simples e segura para consumo B2B.
Projetada para evoluir para planos pagos e rate limiting.
"""

from fastapi import Header, HTTPException, status
from typing import Optional
import os

# -------------------------------------------------
# API KEY CONFIG
# -------------------------------------------------

# Chave padrão para ambiente inicial (DEV / DEMO)
DEFAULT_API_KEY = "gatiflow-demo-key"

# Permite sobrescrever via variável de ambiente
VALID_API_KEYS = {
    os.getenv("GATIFLOW_API_KEY", DEFAULT_API_KEY)
}


# -------------------------------------------------
# Dependency
# -------------------------------------------------

def verify_api_key(x_api_key: Optional[str] = Header(None)) -> str:
    """
    Verifica se a API Key enviada é válida.
    Deve ser usada como dependency nos endpoints protegidos.
    """

    if not x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key missing"
        )

    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key"
        )

    return x_api_key
