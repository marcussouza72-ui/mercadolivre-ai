# MercadoLivre AI SaaS

# 06 - API REST

**Versão:** 1.0.0

**Fase:** Foundation

---

# 1. Objetivo

Este documento descreve os endpoints REST implementados na Fase 1 da aplicação.

Além de documentar as rotas existentes, este documento estabelece o padrão que será utilizado para documentar todos os novos endpoints desenvolvidos nas próximas fases.

---

# 2. Informações Gerais

## Framework

FastAPI

## Arquitetura

RESTful API

## Formato de Dados

JSON

## Autenticação

Bearer Token (JWT)

## Content-Type

```http
application/json
```

---

# 3. Fluxo Geral da API

```text
Cliente

↓

HTTP Request

↓

Router

↓

Service

↓

Repository

↓

Banco de Dados

↓

Repository

↓

Service

↓

HTTP Response
```

---

# 4. Endpoints Implementados

## POST /auth/register

### Objetivo

Cadastrar um novo usuário na plataforma.

### Autenticação

Não requerida.

### Request

```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "password": "SenhaSegura123"
}
```

### Response (201 Created)

```json
{
  "id": "uuid",
  "name": "João Silva",
  "email": "joao@email.com"
}
```

### Possíveis Erros

| HTTP | Motivo |
|------|--------|
| 400 | Dados inválidos |
| 409 | E-mail já cadastrado |

---

## POST /auth/login

### Objetivo

Autenticar um usuário.

### Autenticação

Não requerida.

### Request

```json
{
  "email": "joao@email.com",
  "password": "SenhaSegura123"
}
```

### Response (200 OK)

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}
```

### Possíveis Erros

| HTTP | Motivo |
|------|--------|
| 401 | Credenciais inválidas |
| 403 | Usuário inativo |

---

## POST /auth/refresh

### Objetivo

Renovar os tokens de autenticação.

### Autenticação

Não requerida.

### Request

```json
{
  "refresh_token": "..."
}
```

### Response (200 OK)

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}
```

### Possíveis Erros

| HTTP | Motivo |
|------|--------|
| 401 | Refresh Token inválido |
| 401 | Refresh Token expirado |

---

## GET /auth/me

### Objetivo

Retornar os dados do usuário autenticado.

### Autenticação

Obrigatória.

### Header

```http
Authorization: Bearer <access_token>
```

### Response (200 OK)

```json
{
  "id": "uuid",
  "name": "João Silva",
  "email": "joao@email.com",
  "is_active": true,
  "created_at": "2026-07-20T15:20:00"
}
```

### Possíveis Erros

| HTTP | Motivo |
|------|--------|
| 401 | Token inválido |
| 401 | Token expirado |
| 404 | Usuário não encontrado |

---

# 5. Códigos HTTP Utilizados

| Código | Significado |
|---------|-------------|
| 200 | Requisição executada com sucesso |
| 201 | Recurso criado |
| 400 | Requisição inválida |
| 401 | Não autenticado |
| 403 | Acesso proibido |
| 404 | Recurso não encontrado |
| 409 | Conflito |
| 422 | Erro de validação |
| 500 | Erro interno do servidor |

---

# 6. Convenções da API

A API segue as seguintes convenções:

- Comunicação via JSON.
- Endpoints organizados por domínio.
- Utilização de verbos HTTP apropriados.
- Respostas consistentes.
- Validação de entrada com Pydantic.
- Separação entre modelos de entrada e saída.

---

# 7. Versionamento

Atualmente a API encontra-se na versão inicial da Fase 1.

O versionamento por URL (por exemplo `/api/v1`) poderá ser adotado futuramente caso haja necessidade de manter múltiplas versões simultâneas.

---

# 8. Evolução Prevista

Na Fase 2 serão adicionados novos grupos de endpoints.

Exemplos:

### Mercado Livre

- OAuth
- Contas
- Produtos
- Anúncios
- Pedidos

### Dashboard

- KPIs
- Métricas
- Indicadores

### Inteligência Artificial

- Geração de descrições
- SEO
- Otimização de anúncios
- Recomendações

---

# 9. Boas Práticas

Todos os novos endpoints deverão seguir este padrão de documentação:

- Objetivo
- Método HTTP
- Autenticação
- Request
- Response
- Possíveis erros
- Observações

Essa padronização facilita a manutenção da API e melhora a experiência dos desenvolvedores que utilizam a plataforma.

---

# 10. Conclusão

A API REST da Fase 1 estabelece a base para toda a comunicação entre clientes e servidores da plataforma.

Sua arquitetura privilegia simplicidade, consistência e escalabilidade, permitindo que novos recursos sejam incorporados sem comprometer a organização do sistema.

---

**Documento:** 06_API_REST.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026