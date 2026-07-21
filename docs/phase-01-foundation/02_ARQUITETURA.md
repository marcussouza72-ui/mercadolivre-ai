# MercadoLivre AI SaaS

# 02 - Arquitetura da Aplicação

**Versão:** 1.0.0

**Fase:** Foundation

---

# 1. Objetivo

Este documento descreve a arquitetura adotada no MercadoLivre AI SaaS, apresentando as camadas da aplicação, suas responsabilidades e o fluxo de comunicação entre os componentes.

A arquitetura foi projetada para ser escalável, modular e de fácil manutenção, seguindo boas práticas amplamente utilizadas no desenvolvimento de APIs modernas.

---

# 2. Visão Geral da Arquitetura

A aplicação segue uma arquitetura em camadas (Layered Architecture), com clara separação de responsabilidades.

```text
                Cliente
                   │
                   ▼
        ┌──────────────────┐
        │     FastAPI      │
        └──────────────────┘
                   │
                   ▼
        ┌──────────────────┐
        │     Routers      │
        └──────────────────┘
                   │
                   ▼
        ┌──────────────────┐
        │     Services     │
        └──────────────────┘
                   │
                   ▼
        ┌──────────────────┐
        │  Repositories    │
        └──────────────────┘
                   │
                   ▼
        ┌──────────────────┐
        │   SQLAlchemy     │
        └──────────────────┘
                   │
                   ▼
        ┌──────────────────┐
        │   PostgreSQL     │
        └──────────────────┘
```

Cada camada possui responsabilidades específicas, reduzindo o acoplamento e facilitando a evolução do sistema.

---

# 3. Camadas da Aplicação

## Cliente

Responsável por consumir a API.

Exemplos:

- Frontend Web
- Aplicativo Mobile
- Integrações externas
- Swagger UI

---

## FastAPI

É o ponto de entrada da aplicação.

Responsabilidades:

- Inicializar a aplicação.
- Registrar rotas.
- Configurar middlewares.
- Gerenciar eventos da aplicação.

---

## Routers

Os Routers expõem os endpoints REST.

Responsabilidades:

- Receber requisições HTTP.
- Validar parâmetros.
- Delegar processamento aos Services.
- Retornar respostas.

Os Routers não contêm regras de negócio.

---

## Services

Representam a camada de negócio.

Responsabilidades:

- Implementar regras de negócio.
- Validar processos.
- Coordenar operações.
- Integrar múltiplos repositórios quando necessário.

Toda lógica da aplicação deve permanecer nesta camada.

---

## Repositories

Responsáveis pela persistência dos dados.

Responsabilidades:

- Executar consultas.
- Inserir registros.
- Atualizar dados.
- Excluir registros.

Não devem conter regras de negócio.

---

## SQLAlchemy

Responsável pelo mapeamento objeto-relacional (ORM).

Benefícios:

- Independência do banco.
- Modelagem orientada a objetos.
- Facilidade para migrações.

---

## PostgreSQL

Responsável pelo armazenamento permanente dos dados.

Foi escolhido por oferecer:

- Robustez
- Alto desempenho
- Escalabilidade
- Compatibilidade com SQLAlchemy

---

# 4. Fluxo de uma Requisição

Exemplo de autenticação de usuário.

```text
Cliente

↓

POST /auth/login

↓

Router

↓

UserService.authenticate()

↓

UserRepository

↓

PostgreSQL

↓

UserRepository

↓

UserService

↓

JWT

↓

Resposta HTTP
```

Esse fluxo evidencia a separação entre apresentação, negócio e persistência.

---

# 5. Padrões Arquiteturais

Durante a Fase 1 foram adotados os seguintes padrões.

## Repository Pattern

Isola o acesso ao banco de dados.

Benefícios:

- Baixo acoplamento.
- Facilidade para testes.
- Reutilização de código.

---

## Service Layer

Centraliza toda a lógica de negócio.

Benefícios:

- Organização.
- Reutilização.
- Facilidade para manutenção.

---

## Dependency Injection

Utilizada para fornecer dependências aos componentes da aplicação.

Benefícios:

- Baixo acoplamento.
- Maior testabilidade.
- Código mais limpo.

---

# 6. Fluxo de Autenticação

```text
Cadastro

↓

Hash da senha (Argon2)

↓

Banco de Dados

↓

Login

↓

Validação da senha

↓

JWT Access Token

+

Refresh Token

↓

Cliente

↓

Requisições autenticadas

↓

Refresh Token

↓

Novos Tokens
```

---

# 7. Benefícios da Arquitetura

A arquitetura escolhida oferece:

- Separação de responsabilidades.
- Facilidade de manutenção.
- Escalabilidade.
- Testabilidade.
- Reutilização de código.
- Facilidade para integração com APIs externas.

---

# 8. Evolução Prevista

A arquitetura foi preparada para receber novos módulos, incluindo:

- Integração Mercado Livre.
- Inteligência Artificial.
- Dashboards.
- Filas de processamento.
- Cache.
- Webhooks.
- Multiempresa.
- Integrações com novos marketplaces.

Esses módulos poderão ser adicionados sem alterações estruturais significativas.

---

# 9. Conclusão

A arquitetura adotada fornece uma base sólida para o crescimento do sistema.

A separação entre apresentação, regras de negócio e persistência reduz o acoplamento, melhora a organização do código e facilita futuras expansões.

---

**Documento:** 02_ARQUITETURA.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026