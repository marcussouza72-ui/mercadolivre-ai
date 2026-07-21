from pydantic import BaseModel


class MercadoLivreConnectionResponse(BaseModel):
    """
    Resposta da conexão de uma conta Mercado Livre.
    """

    success: bool
    message: str
    nickname: str
    ml_user_id: int