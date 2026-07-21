from __future__ import annotations

from .common import MercadoLivreSchema


class MercadoLivreItemsSearchResponse(MercadoLivreSchema):
    """
    Resposta do endpoint:

    GET /users/{user_id}/items/search
    """

    results: list[str]


class MercadoLivreItem(MercadoLivreSchema):
    """
    Informações básicas de um anúncio.

    Inicialmente modelamos apenas os campos mais utilizados.
    Novos atributos serão adicionados conforme o projeto evoluir.
    """

    id: str
    site_id: str
    title: str

    category_id: str | None = None

    price: float

    currency_id: str

    available_quantity: int

    sold_quantity: int

    buying_mode: str | None = None

    listing_type_id: str | None = None

    condition: str | None = None

    permalink: str | None = None

    status: str | None = None

    accepts_mercadopago: bool | None = None

    catalog_listing: bool | None = None