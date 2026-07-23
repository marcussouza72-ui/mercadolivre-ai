from __future__ import annotations


class MercadoLivreError(Exception):
    """
    Exceção base para erros relacionados à integração
    com o Mercado Livre.
    """


class InvalidOAuthStateError(MercadoLivreError):
    """
    OAuth State inválido, expirado ou já utilizado.
    """


class MLAccountAlreadyLinkedError(MercadoLivreError):
    """
    A conta do Mercado Livre já está vinculada
    a outro usuário da aplicação.
    """