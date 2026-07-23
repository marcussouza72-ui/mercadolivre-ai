from pydantic import BaseModel


class MercadoLivreAuthorizationResponse(BaseModel):
    """
    Resposta contendo a URL para iniciar
    o fluxo OAuth do Mercado Livre.
    """

    authorization_url: str


class MercadoLivreConnectionResponse(BaseModel):
    """
    Resposta da conexão de uma conta Mercado Livre.
    """

    success: bool
    message: str
    nickname: str
    ml_user_id: int