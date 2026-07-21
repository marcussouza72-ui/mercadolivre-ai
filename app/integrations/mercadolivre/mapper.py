from __future__ import annotations

from app.integrations.mercadolivre.schemas.items import MercadoLivreItem
from app.models.ml_item import MLItem


class MercadoLivreMapper:
    """
    Responsável por converter Schemas da API do Mercado Livre
    em entidades da aplicação.
    """

    @staticmethod
    def to_ml_item(
        item: MercadoLivreItem,
        *,
        account_id,
    ) -> MLItem:
        """
        Converte um MercadoLivreItem em um novo MLItem.
        """

        return MLItem(
            account_id=account_id,
            ml_item_id=item.id,
            title=item.title,
            category_id=item.category_id,
            listing_type_id=item.listing_type_id,
            condition=item.condition,
            status=item.status,
            permalink=item.permalink,
            price=item.price,
            currency_id=item.currency_id,
            available_quantity=item.available_quantity,
            sold_quantity=item.sold_quantity,
            accepts_mercadopago=item.accepts_mercadopago
            if item.accepts_mercadopago is not None
            else True,
            catalog_listing=item.catalog_listing
            if item.catalog_listing is not None
            else False,
        )

    @staticmethod
    def update_ml_item(
        model: MLItem,
        item: MercadoLivreItem,
    ) -> MLItem:
        """
        Atualiza um MLItem existente utilizando os dados
        retornados pela API do Mercado Livre.
        """

        model.title = item.title
        model.category_id = item.category_id
        model.listing_type_id = item.listing_type_id
        model.condition = item.condition
        model.status = item.status
        model.permalink = item.permalink
        model.price = item.price
        model.currency_id = item.currency_id
        model.available_quantity = item.available_quantity
        model.sold_quantity = item.sold_quantity
        model.accepts_mercadopago = (
            item.accepts_mercadopago
            if item.accepts_mercadopago is not None
            else True
        )
        model.catalog_listing = (
            item.catalog_listing
            if item.catalog_listing is not None
            else False
        )

        return model