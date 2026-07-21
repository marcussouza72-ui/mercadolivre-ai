# MercadoLivre AI SaaS

## Documentação Oficial

**Versão:** 1.0.0  
**Fase:** 01 - Foundation  
**Status:** Concluída

---

# Objetivo da Documentação

Esta documentação registra todas as decisões técnicas tomadas durante o desenvolvimento da Fase 1 do projeto MercadoLivre AI SaaS.

Ela servirá como referência oficial para:

- Desenvolvimento futuro
- Onboarding de novos desenvolvedores
- Consulta técnica
- Base de conhecimento para IA (NotebookLM)
- Histórico da evolução da arquitetura

---

# Sobre o Projeto

O MercadoLivre AI SaaS é uma plataforma desenvolvida para vendedores profissionais de marketplaces.

Seu objetivo é centralizar em um único sistema a gestão operacional, comercial e analítica de contas do Mercado Livre, utilizando Inteligência Artificial para automatizar processos, gerar insights e aumentar a eficiência operacional.

A arquitetura foi concebida para permitir futura expansão para outros marketplaces, como Shopee, Amazon e Magalu.

---

# Tecnologias Utilizadas

## Backend

- Python 3.12
- FastAPI
- SQLAlchemy 2
- Alembic
- PostgreSQL

## Segurança

- JWT
- Refresh Token Rotation
- Argon2 (pwdlib)

## Arquitetura

- Repository Pattern
- Service Layer
- Dependency Injection
- Arquitetura Modular

---

# Documentos da Fase 1

| Documento | Descrição |
|------------|-----------|
| 01_VISAO_GERAL.md | Visão geral do projeto |
| 02_ARQUITETURA.md | Arquitetura da aplicação |
| 03_ESTRUTURA_DO_PROJETO.md | Organização dos módulos |
| 04_BANCO_DE_DADOS.md | Modelagem do banco de dados |
| 05_AUTENTICACAO_E_SEGURANCA.md | Autenticação e segurança |
| 06_API_REST.md | Endpoints da API |
| 07_DECISOES_DE_ARQUITETURA.md | Decisões técnicas adotadas |
| 08_ROADMAP_FASE_02.md | Planejamento da próxima fase |
| CHANGELOG_FASE_01.md | Histórico da Fase 1 |

---

# Escopo da Fase 1

Durante esta fase foram implementados:

- Estrutura inicial do projeto
- Configuração do FastAPI
- PostgreSQL
- SQLAlchemy 2
- Alembic
- Repository Pattern
- Service Layer
- Dependency Injection
- Sistema de autenticação JWT
- Hash de senhas com Argon2
- Access Token
- Refresh Token
- Refresh Token Rotation

---

# Próxima Fase

A Fase 2 será dedicada à integração com a API do Mercado Livre, incluindo:

- OAuth 2.0
- Conexão de múltiplas contas
- Sincronização de anúncios
- Sincronização de pedidos
- Gestão automática de tokens
- Dashboard operacional

---

**Documento:** 00_SUMARIO.md

**Versão:** 1.0.0