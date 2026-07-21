"""
Catálogo oficial de endpoints da API do Mercado Livre.

Toda comunicação com a API deve utilizar estas constantes.
Nunca escreva URLs diretamente nos Services ou Repositories.
"""

# ==========================================================
# Base URLs
# ==========================================================

API_BASE_URL = "https://api.mercadolibre.com"

AUTH_BASE_URL = "https://auth.mercadolivre.com.br"


# ==========================================================
# OAuth
# ==========================================================

OAUTH_AUTHORIZE = "/authorization"

OAUTH_TOKEN = "/oauth/token"


# ==========================================================
# Usuários
# ==========================================================

USERS_ME = "/users/me"


# ==========================================================
# Itens / Anúncios
# ==========================================================

ITEMS = "/items"

ITEM = "/items/{item_id}"

ITEM_DESCRIPTION = "/items/{item_id}/description"

ITEM_PRICES = "/items/{item_id}/prices"


# ==========================================================
# Orders
# ==========================================================

ORDERS = "/orders"

ORDER = "/orders/{order_id}"


# ==========================================================
# Questions
# ==========================================================

QUESTIONS = "/questions/search"


# ==========================================================
# Shipments
# ==========================================================

SHIPMENTS = "/shipments/{shipment_id}"


# ==========================================================
# Categories
# ==========================================================

CATEGORIES = "/categories/{category_id}"


# ==========================================================
# Sites
# ==========================================================

SITES = "/sites"

SITE = "/sites/{site_id}"


# ==========================================================
# Trends
# ==========================================================

TRENDS = "/trends/{site_id}"


# ==========================================================
# Currency
# ==========================================================

CURRENCIES = "/currencies"

CURRENCY = "/currencies/{currency_id}"