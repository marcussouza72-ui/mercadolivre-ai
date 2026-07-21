# MercadoLivre AI SaaS

# 07 - Decisões de Arquitetura

**Versão:** 1.0.0

**Fase:** Foundation

---

# 1. Objetivo

Este documento registra as principais decisões arquiteturais tomadas durante a Fase 1 do projeto.

O objetivo é preservar o contexto técnico de cada escolha, facilitando futuras evoluções da plataforma e evitando decisões inconsistentes ao longo do desenvolvimento.

---

# 2. Decisão 001 — FastAPI como Framework Principal

## Contexto

Era necessário escolher um framework moderno para desenvolvimento de APIs REST.

## Decisão

Foi adotado o FastAPI como framework principal da aplicação.

## Justificativa

- Alto desempenho.
- Suporte nativo à tipagem do Python.
- Documentação automática com OpenAPI.
- Excelente integração com Pydantic.
- Forte adoção pela comunidade.

## Consequências

- Desenvolvimento mais rápido.
- Documentação automática.
- Facilidade de integração com ferramentas modernas.

---

# 3. Decisão 002 — PostgreSQL

## Contexto

Era necessário escolher um banco de dados relacional para suportar o crescimento do sistema.

## Decisão

Foi adotado PostgreSQL.

## Justificativa

- Banco robusto.
- Suporte completo a transações ACID.
- Excelente desempenho.
- Compatibilidade com SQLAlchemy.
- Escalabilidade comprovada.

## Consequências

- Base sólida para futuras integrações.
- Facilidade de manutenção.

---

# 4. Decisão 003 — SQLAlchemy 2

## Contexto

A aplicação precisava de um ORM moderno.

## Decisão

Utilizar SQLAlchemy 2.

## Justificativa

- ORM maduro.
- Alto nível de flexibilidade.
- Excelente integração com Alembic.
- Ampla documentação.

## Consequências

- Código desacoplado do banco.
- Facilidade para migrações.

---

# 5. Decisão 004 — Repository Pattern

## Contexto

Era necessário separar regras de negócio da persistência.

## Decisão

Adotar Repository Pattern.

## Justificativa

- Baixo acoplamento.
- Facilidade para testes.
- Reutilização de consultas.
- Melhor organização.

## Consequências

- Código mais limpo.
- Evolução facilitada.

---

# 6. Decisão 005 — Service Layer

## Contexto

As regras de negócio não deveriam ficar nos endpoints.

## Decisão

Criar uma camada exclusiva para serviços.

## Justificativa

- Centralização das regras de negócio.
- Reutilização.
- Facilidade de manutenção.

## Consequências

- Routers simplificados.
- Código mais organizado.

---

# 7. Decisão 006 — Dependency Injection

## Contexto

Era necessário reduzir o acoplamento entre componentes.

## Decisão

Utilizar o mecanismo de Dependency Injection do FastAPI.

## Justificativa

- Reutilização.
- Facilidade para testes.
- Separação de responsabilidades.

## Consequências

- Componentes mais independentes.
- Maior flexibilidade.

---

# 8. Decisão 007 — UUID como Chave Primária

## Contexto

O sistema deverá suportar crescimento e múltiplas integrações.

## Decisão

Utilizar UUID em todas as entidades.

## Justificativa

- Identificadores únicos.
- Maior segurança.
- Melhor suporte para arquitetura distribuída.

## Consequências

- Dificulta enumeração de registros.
- Facilita futuras integrações.

---

# 9. Decisão 008 — Argon2

## Contexto

Era necessário escolher um algoritmo moderno para proteção de senhas.

## Decisão

Utilizar Argon2 por meio da biblioteca pwdlib.

## Justificativa

- Recomendado atualmente para novas aplicações.
- Alta resistência a ataques.
- Configuração segura.

## Consequências

- Maior segurança das credenciais.
- Facilidade de atualização futura.

---

# 10. Decisão 009 — JWT Stateless

## Contexto

A autenticação deveria ser escalável e independente de sessões armazenadas no servidor.

## Decisão

Utilizar JWT.

## Justificativa

- Escalabilidade.
- Simplicidade.
- Excelente integração com APIs.

## Consequências

- Não há armazenamento de sessão no servidor.
- Renovação realizada por Refresh Token.

---

# 11. Decisão 010 — Refresh Token Rotation

## Contexto

Era necessário permitir renovação segura da sessão.

## Decisão

Implementar Refresh Token Rotation.

## Justificativa

- Redução de riscos.
- Renovação transparente para o usuário.
- Base para futuras estratégias de revogação.

## Consequências

- Maior segurança.
- Arquitetura preparada para OAuth.

---

# 12. Decisão 011 — Arquitetura Modular

## Contexto

O sistema deverá crescer continuamente.

## Decisão

Organizar o projeto em módulos independentes.

## Justificativa

- Escalabilidade.
- Organização.
- Facilidade para manutenção.

## Consequências

- Crescimento sustentável.
- Menor impacto entre módulos.

---

# 13. Lições Aprendidas

Durante a Fase 1 foram observados os seguintes pontos:

- A definição de uma arquitetura sólida no início reduz retrabalho.
- A separação clara entre camadas simplifica o desenvolvimento.
- A documentação contínua facilita a manutenção do projeto.
- A adoção de padrões consistentes melhora a qualidade do código.

---

# 14. Decisões para Revisão Futura

As seguintes decisões poderão ser reavaliadas conforme a evolução do projeto:

- Estratégia de versionamento da API.
- Introdução de cache distribuído.
- Uso de filas assíncronas.
- Arquitetura orientada a eventos.
- Estratégia de observabilidade e monitoramento.

Essas revisões deverão ocorrer somente quando houver necessidade comprovada.

---

# 15. Conclusão

As decisões arquiteturais registradas neste documento formam a base técnica da plataforma.

Toda nova funcionalidade deverá respeitar esses princípios ou, quando necessário, justificar formalmente novas decisões arquiteturais.

---

**Documento:** 07_DECISOES_DE_ARQUITETURA.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026