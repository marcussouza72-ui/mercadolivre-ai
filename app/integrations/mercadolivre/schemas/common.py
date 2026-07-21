from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class MercadoLivreSchema(BaseModel):
    """
    Classe base para todos os schemas da API do Mercado Livre.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
    )