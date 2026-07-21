# MercadoLivre AI SaaS

# 03 - Estrutura do Projeto

**Versão:** 1.0.0

**Fase:** Foundation

---

# 1. Objetivo

Este documento descreve a organização física do projeto, apresentando a estrutura de diretórios adotada, a responsabilidade de cada módulo e as convenções utilizadas para manter o código organizado, escalável e de fácil manutenção.

---

# 2. Estrutura Geral

A estrutura principal do projeto é organizada da seguinte forma:

```text
mercadolivre-ai/
├── alembic/
├── app/
├── docs/
├── tests/
├── .env
├── alembic.ini
├── README.md
├── requirements.txt
└── runtime.txt
```

Cada diretório possui uma responsabilidade específica, evitando mistura entre código, documentação, testes e arquivos de configuração.

---

# 3. Diretório app/

O diretório `app` contém todo o código-fonte da aplicação.

```text
app/
├── ai/
├── analytics/
├── api/
├── auth/
├── core/
├── database/
├── dependencies/
├── exceptions/
├── integrations/
├── models/
├── repositories/
├── routers/
├── schemas/
├── services/
└── utils/
```

---

# 4. Responsabilidade de Cada Pasta

## ai/

Destinada aos módulos de Inteligência Artificial.

Exemplos futuros:

- geração de descrições
- análise de anúncios
- classificação automática
- agentes inteligentes

---

## analytics/

Responsável por indicadores, métricas e análises.

Exemplos:

- KPIs
- dashboards
- relatórios
- métricas comerciais

---

## api/

Componentes relacionados à configuração geral da API.

Exemplos:

- inicialização
- versão da API
- configuração global

---

## auth/

Responsável por autenticação e autorização.

Contém:

- JWT
- geração de tokens
- validação de tokens
- hash de senhas
- autenticação

---

## core/

Configurações centrais do sistema.

Exemplos:

- Settings
- variáveis de ambiente
- constantes
- configurações globais

---

## database/

Responsável pela infraestrutura do banco.

Contém:

- conexão
- sessão
- BaseModel
- inicialização do ORM

---

## dependencies/

Dependências reutilizáveis do FastAPI.

Exemplos:

- usuário autenticado
- sessão do banco
- permissões

---

## exceptions/

Exceções personalizadas e tratamento global de erros.

---

## integrations/

Integrações com sistemas externos.

Exemplos futuros:

- Mercado Livre
- Shopee
- Amazon
- OpenAI
- serviços de pagamento

---

## models/

Modelos do SQLAlchemy.

Representam as tabelas do banco de dados.

---

## repositories/

Camada responsável pelo acesso ao banco de dados.

Funções:

- consultas
- inserções
- atualizações
- remoções

Não contém regras de negócio.

---

## routers/

Endpoints da API REST.

Responsabilidades:

- receber requisições
- validar entrada
- chamar Services
- retornar respostas

---

## schemas/

Modelos Pydantic.

Responsáveis por:

- validação
- serialização
- documentação da API

---

## services/

Camada de regras de negócio.

Toda lógica da aplicação deve permanecer nesta camada.

Exemplos:

- autenticação
- cadastro
- integrações
- validações

---

## utils/

Funções auxiliares reutilizáveis.

Exemplos:

- datas
- conversões
- utilidades
- helpers

---

# 5. Diretório docs/

Armazena toda a documentação técnica do projeto.

Organização prevista:

```text
docs/
├── phase-01-foundation/
├── phase-02-mercadolivre/
├── phase-03-ai/
└── phase-04-scale/
```

Cada fase possuirá sua documentação própria.

---

# 6. Diretório tests/

Responsável pelos testes automatizados.

Estrutura prevista:

```text
tests/
├── unit/
├── integration/
└── fixtures/
```

---

# 7. Convenções Adotadas

Durante o desenvolvimento deverão ser seguidas as seguintes convenções.

## Separação de Responsabilidades

Cada módulo deve possuir apenas uma responsabilidade principal.

---

## Modularidade

Novas funcionalidades deverão ser adicionadas em módulos específicos.

---

## Reutilização

Sempre que possível, funções reutilizáveis deverão ser centralizadas.

---

## Organização

Evitar arquivos excessivamente grandes.

Quando um módulo crescer significativamente, deverá ser subdividido.

---

# 8. Crescimento da Estrutura

A arquitetura foi planejada para permitir expansão sem reorganizações estruturais.

Novos módulos poderão ser adicionados mantendo a mesma organização.

Exemplos:

- notifications/
- webhooks/
- billing/
- reports/
- workers/
- cache/

---

# 9. Conclusão

A estrutura adotada prioriza organização, clareza e escalabilidade.

Essa organização reduz o acoplamento entre os componentes e facilita a evolução contínua da aplicação conforme novas funcionalidades forem sendo incorporadas.

---

**Documento:** 03_ESTRUTURA_DO_PROJETO.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026