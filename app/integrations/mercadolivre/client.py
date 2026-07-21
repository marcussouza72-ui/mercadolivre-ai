from __future__ import annotations

from typing import Any

import httpx


class MercadoLivreClient:
    """
    Cliente HTTP assíncrono responsável por toda a comunicação
    com a API do Mercado Livre.

    Esta classe abstrai o uso do httpx.AsyncClient e centraliza
    todas as requisições HTTP da integração.
    """

    def __init__(
        self,
        base_url: str,
        timeout: float = 30.0,
    ) -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            headers={
                "Accept": "application/json",
            },
        )

    @staticmethod
    def _build_headers(
        headers: dict[str, str] | None = None,
        access_token: str | None = None,
    ) -> dict[str, str]:
        """
        Monta os headers finais da requisição.
        """

        final_headers = dict(headers or {})

        if access_token:
            final_headers["Authorization"] = f"Bearer {access_token}"

        return final_headers

    async def get(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
        access_token: str | None = None,
    ) -> httpx.Response:
        return await self._client.get(
            url,
            headers=self._build_headers(headers, access_token),
            params=params,
        )

    async def post(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        access_token: str | None = None,
    ) -> httpx.Response:
        return await self._client.post(
            url,
            headers=self._build_headers(headers, access_token),
            json=json,
            data=data,
        )

    async def put(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        json: dict[str, Any] | None = None,
        access_token: str | None = None,
    ) -> httpx.Response:
        return await self._client.put(
            url,
            headers=self._build_headers(headers, access_token),
            json=json,
        )

    async def delete(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        access_token: str | None = None,
    ) -> httpx.Response:
        return await self._client.delete(
            url,
            headers=self._build_headers(headers, access_token),
        )

    async def close(self) -> None:
        """
        Fecha o cliente HTTP.
        """
        await self._client.aclose()