# MercadoLivre AI SaaS

# 04 - Banco de Dados

**Versão:** 1.0.0

**Fase:** Foundation

---

# 1. Objetivo

Este documento descreve a arquitetura da camada de persistência do MercadoLivre AI SaaS, incluindo o banco de dados adotado, o ORM utilizado, o modelo base das entidades, as convenções de nomenclatura e a estratégia de migração de esquema.

A camada de persistência foi projetada para oferecer escalabilidade, consistência e facilidade de manutenção.

---

# 2. Tecnologias Utilizadas

## Banco de Dados

- PostgreSQL

## ORM

- SQLAlchemy 2

## Migrações

- Alembic

---

# 3. Escolha do PostgreSQL

O PostgreSQL foi escolhido por oferecer:

- Alta confiabilidade
- Excelente desempenho
- Suporte completo a transações ACID
- Grande compatibilidade com SQLAlchemy
- Recursos avançados para crescimento futuro
- Amplo suporte da comunidade

A escolha permite que o sistema cresça sem necessidade de troca de banco de dados.

---

# 4. SQLAlchemy 2

O SQLAlchemy é responsável pelo mapeamento objeto-relacional (ORM).

Principais benefícios:

- Abstração do banco de dados
- Modelagem orientada a objetos
- Consultas seguras
- Reutilização de código
- Facilidade para testes
- Integração nativa com Alembic

---

# 5. BaseModel

Todas as entidades do sistema herdam de uma classe base comum.

Essa abordagem padroniza atributos compartilhados e reduz duplicação de código.

A BaseModel possui os seguintes campos:

| Campo | Descrição |
|--------|-----------|
| id | Identificador UUID |
| created_at | Data de criação |
| updated_at | Data da última atualização |

Essa estratégia garante consistência entre todas as tabelas.

---

# 6. Identificadores UUID

Foi adotado UUID como chave primária para todas as entidades.

## Vantagens

- Identificadores globalmente únicos
- Maior segurança
- Dificulta enumeração de registros
- Facilita integrações distribuídas
- Preparado para arquitetura multiempresa

---

# 7. Convenções de Modelagem

As seguintes convenções deverão ser utilizadas em todas as entidades.

## Nome das tabelas

- letras minúsculas
- plural quando apropriado
- nomes descritivos

Exemplos:

```text
users
products
orders
accounts
```

---

## Nome das colunas

Utilizar padrão snake_case.

Exemplos:

```text
created_at
updated_at
first_name
access_token
refresh_token
```

---

## Chaves estrangeiras

Sempre utilizar UUID.

Exemplo:

```text
user_id
account_id
product_id
```

---

# 8. Migrações com Alembic

Toda alteração estrutural deverá ser realizada através do Alembic.

Fluxo adotado:

```text
Modelo SQLAlchemy

↓

Alembic Revision

↓

Migração

↓

Banco de Dados
```

Nenhuma alteração estrutural deverá ser realizada manualmente diretamente no banco de dados.

---

# 9. Estrutura Inicial

Na conclusão da Fase 1, o banco possui a seguinte entidade principal.

## User

Responsável pelo gerenciamento de usuários da plataforma.

Principais informações armazenadas:

- identificador
- nome
- e-mail
- senha criptografada
- status
- datas de auditoria

Essa entidade será utilizada como base para autenticação e autorização.

---

# 10. Evolução Prevista

Durante as próximas fases serão adicionadas novas entidades.

Exemplos:

- MercadoLivreAccount
- Product
- Listing
- Order
- Customer
- Shipment
- Notification
- AIRequest
- Analytics
- AuditLog

A estrutura atual foi planejada para suportar essa expansão sem necessidade de mudanças estruturais significativas.

---

# 11. Boas Práticas

Durante o desenvolvimento deverão ser observadas as seguintes práticas:

- Nunca alterar tabelas diretamente em produção.
- Toda mudança estrutural deve possuir migração Alembic.
- Evitar duplicação de dados.
- Utilizar relacionamentos corretamente.
- Manter consistência referencial.
- Documentar novas entidades ao final de cada fase.

---

# 12. Conclusão

A camada de persistência foi projetada para ser robusta, organizada e preparada para crescimento contínuo.

A utilização de PostgreSQL, SQLAlchemy 2 e Alembic fornece uma base sólida para suportar novas funcionalidades, integrações e aumento do volume de dados ao longo da evolução do projeto.

---

**Documento:** 04_BANCO_DE_DADOS.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026