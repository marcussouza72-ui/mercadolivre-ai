# MercadoLivre AI SaaS

# 01 - Visão Geral do Projeto

**Versão:** 1.0.0

**Fase:** Foundation

---

# 1. Objetivo

O MercadoLivre AI SaaS é uma plataforma SaaS (Software as a Service) desenvolvida para vendedores profissionais de marketplaces.

Seu principal objetivo é centralizar operações, automatizar processos e fornecer inteligência analítica baseada em Inteligência Artificial para aumentar produtividade, reduzir tarefas manuais e apoiar decisões estratégicas.

Embora a primeira integração seja com o Mercado Livre, toda a arquitetura foi planejada para suportar múltiplos marketplaces no futuro.

---

# 2. Visão de Longo Prazo

A plataforma pretende se tornar um hub completo de gestão para e-commerce, oferecendo recursos como:

- Gestão de anúncios
- Gestão de pedidos
- Gestão financeira
- Indicadores de desempenho
- Automações operacionais
- Inteligência Artificial aplicada ao negócio
- Gestão de múltiplas contas
- Integração com diversos marketplaces

O sistema será modular, permitindo a expansão contínua sem necessidade de grandes refatorações estruturais.

---

# 3. Público-Alvo

O sistema foi projetado para atender principalmente:

- Pequenos vendedores
- Médios vendedores
- Grandes operações de e-commerce
- Agências que administram contas de terceiros
- Empresas com múltiplos CNPJs
- Operadores de marketplace

---

# 4. Objetivos da Plataforma

Os principais objetivos do projeto são:

- Centralizar informações em um único sistema.
- Automatizar tarefas repetitivas.
- Reduzir tempo operacional.
- Melhorar a tomada de decisão por meio de indicadores.
- Utilizar Inteligência Artificial para auxiliar o vendedor.
- Construir uma plataforma escalável e preparada para crescimento.

---

# 5. Princípios de Arquitetura

Durante o desenvolvimento foram definidos alguns princípios fundamentais.

## Escalabilidade

Cada módulo deve poder crescer de forma independente.

## Modularidade

As funcionalidades são organizadas em módulos com responsabilidades bem definidas.

## Baixo Acoplamento

As regras de negócio não dependem diretamente do banco de dados nem da camada HTTP.

## Alta Coesão

Cada componente possui uma responsabilidade específica.

## Facilidade de Testes

A arquitetura deve permitir testes unitários e testes de integração.

## Manutenibilidade

Novas funcionalidades devem ser adicionadas com o menor impacto possível no restante do sistema.

---

# 6. Tecnologias Adotadas

## Linguagem

- Python 3.12

## Framework Web

- FastAPI

## Banco de Dados

- PostgreSQL

## ORM

- SQLAlchemy 2

## Migrações

- Alembic

## Segurança

- JWT
- Refresh Token
- Argon2 (pwdlib)

---

# 7. Estrutura Geral da Solução

A arquitetura está organizada em camadas.

```text
Cliente

↓

API REST (FastAPI)

↓

Routers

↓

Services

↓

Repositories

↓

SQLAlchemy

↓

PostgreSQL
```

Essa separação reduz o acoplamento entre as camadas e facilita manutenção e evolução do sistema.

---

# 8. Escopo da Fase 1

Nesta fase foram implementados:

- Estrutura inicial do projeto
- Configuração do FastAPI
- Configuração do PostgreSQL
- SQLAlchemy 2
- Alembic
- BaseModel
- UUID
- Repository Pattern
- Service Layer
- Dependency Injection
- Sistema de autenticação
- JWT
- Refresh Token Rotation

---

# 9. Próximas Etapas

A próxima fase será dedicada à integração com a API do Mercado Livre.

Os principais módulos previstos são:

- OAuth 2.0
- Gestão de múltiplas contas
- Sincronização de anúncios
- Sincronização de pedidos
- Gestão automática de tokens
- Dashboard operacional

---

# 10. Conclusão

A Fase 1 estabeleceu uma base sólida para o desenvolvimento da plataforma.

A arquitetura adotada prioriza escalabilidade, organização, segurança e facilidade de manutenção, permitindo que as próximas funcionalidades sejam implementadas de forma incremental e sustentável.

---

**Documento:** 01_VISAO_GERAL.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026