from __future__ import annotations

from app.integrations.mercadolivre.token_manager import TokenManager
from app.schemas.ml_account import MLAccountCreate, MLAccountUpdate


class MercadoLivreMapper:
    """
    Converte respostas da API do Mercado Livre
    em schemas internos da aplicação.
    """

    @staticmethod
    def to_create(
        *,
        profile: dict,
        oauth: dict,
    ) -> MLAccountCreate:
        """
        Converte os dados retornados pelo OAuth
        e pelo endpoint /users/me para MLAccountCreate.
        """

        return MLAccountCreate(
            ml_user_id=profile["id"],
            nickname=profile["nickname"],
            site_id=profile["site_id"],
            access_token=oauth["access_token"],
            refresh_token=oauth["refresh_token"],
            token_type=oauth["token_type"],
            scope=oauth.get("scope"),
            expires_at=TokenManager.expires_at(
                oauth["expires_in"],
            ),
            is_active=True,
        )

    @staticmethod
    def to_update(
        *,
        oauth: dict,
    ) -> MLAccountUpdate:
        """
        Converte os dados OAuth
        para MLAccountUpdate.
        """

        return MLAccountUpdate(
            access_token=oauth["access_token"],
            refresh_token=oauth["refresh_token"],
            token_type=oauth["token_type"],
            scope=oauth.get("scope"),
            expires_at=TokenManager.expires_at(
                oauth["expires_in"],
            ),
        )