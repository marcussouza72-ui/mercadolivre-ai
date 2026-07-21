"""
Exceções específicas da integração com o Mercado Livre.
"""


class MercadoLivreError(Exception):
    """Classe base para todas as exceções da integração."""

    pass


class MercadoLivreAuthenticationError(MercadoLivreError):
    """Erro de autenticação."""

    pass


class MercadoLivreAuthorizationError(MercadoLivreError):
    """Usuário sem permissão para acessar o recurso."""

    pass


class MercadoLivreNotFoundError(MercadoLivreError):
    """Recurso não encontrado."""

    pass


class MercadoLivreRateLimitError(MercadoLivreError):
    """Limite de requisições excedido."""

    pass


class MercadoLivreValidationError(MercadoLivreError):
    """Erro de validação retornado pela API."""

    pass


class MercadoLivreServerError(MercadoLivreError):
    """Erro interno do Mercado Livre."""

    pass


class MercadoLivreUnexpectedError(MercadoLivreError):
    """Erro inesperado durante a comunicação com a API."""

    pass