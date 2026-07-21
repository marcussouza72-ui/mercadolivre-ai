# MercadoLivre AI SaaS

# 08 - Roadmap da Fase 2

**Versão:** 1.0.0

**Fase Atual:** Foundation

**Próxima Fase:** Integração Mercado Livre

---

# 1. Objetivo

Este documento apresenta o planejamento técnico da Fase 2 do MercadoLivre AI SaaS.

O objetivo desta fase é integrar completamente a plataforma à API do Mercado Livre, estabelecendo a infraestrutura necessária para sincronização de dados, automação operacional e futuras funcionalidades baseadas em Inteligência Artificial.

---

# 2. Objetivos da Fase 2

Ao final desta fase o sistema deverá ser capaz de:

- Conectar contas do Mercado Livre.
- Gerenciar múltiplas contas por usuário.
- Sincronizar anúncios.
- Sincronizar pedidos.
- Sincronizar perguntas.
- Sincronizar categorias.
- Gerenciar tokens OAuth automaticamente.
- Disponibilizar dados para os módulos analíticos.

---

# 3. Macroarquitetura

A Fase 2 introduzirá uma nova camada de integração.

```text
Cliente

↓

FastAPI

↓

Services

↓

Integrações Mercado Livre

↓

API Mercado Livre

↓

Banco de Dados
```

Essa camada será responsável por isolar toda a comunicação com APIs externas.

---

# 4. Módulos Planejados

## 4.1 OAuth

Responsável por:

- autorização do usuário;
- troca de código por token;
- armazenamento seguro dos tokens;
- renovação automática.

---

## 4.2 Contas

Gerenciamento de múltiplas contas Mercado Livre por usuário.

Principais funcionalidades:

- conectar conta;
- listar contas;
- remover conta;
- identificar conta principal.

---

## 4.3 Produtos

Sincronização do catálogo.

Informações previstas:

- título;
- preço;
- estoque;
- status;
- categoria;
- atributos;
- imagens.

---

## 4.4 Anúncios

Gerenciamento dos anúncios publicados.

Recursos previstos:

- sincronização;
- atualização;
- métricas;
- desempenho.

---

## 4.5 Pedidos

Importação automática dos pedidos.

Dados previstos:

- comprador;
- produtos;
- valores;
- frete;
- status.

---

## 4.6 Perguntas

Importação das perguntas realizadas pelos compradores.

Futuramente serão utilizadas pela IA para geração de respostas automáticas.

---

## 4.7 Métricas

Coleta de indicadores operacionais.

Exemplos:

- vendas;
- faturamento;
- visitas;
- conversão;
- reputação.

---

# 5. Novas Entidades

Durante a Fase 2 deverão ser adicionadas entidades como:

- MercadoLivreAccount
- Listing
- Product
- Order
- OrderItem
- Customer
- Shipment
- Question
- Category
- OAuthToken

Todas seguirão os padrões definidos na documentação da Fase 1.

---

# 6. Segurança

Além da autenticação própria da plataforma, será implementado o OAuth 2.0 do Mercado Livre.

Os tokens do Mercado Livre serão armazenados separadamente dos tokens JWT utilizados pela aplicação.

Essa separação reduz riscos e simplifica o gerenciamento das credenciais.

---

# 7. Arquitetura das Integrações

As integrações seguirão a seguinte organização:

```text
integrations/

└── mercadolivre/
    ├── client.py
    ├── auth.py
    ├── products.py
    ├── orders.py
    ├── questions.py
    ├── categories.py
    └── utils.py
```

Cada módulo será responsável por um domínio específico da API do Mercado Livre.

---

# 8. Critérios de Conclusão

A Fase 2 será considerada concluída quando:

- OAuth estiver funcional.
- Contas puderem ser conectadas.
- Tokens forem renovados automaticamente.
- Produtos estiverem sincronizados.
- Pedidos estiverem sincronizados.
- Estrutura preparada para IA.

---

# 9. Dependências para a Fase 3

A Fase 3 utilizará os dados obtidos nesta fase para:

- geração de descrições;
- otimização SEO;
- análise de anúncios;
- recomendações;
- automações inteligentes.

Sem a infraestrutura da Fase 2 essas funcionalidades não poderão ser implementadas.

---

# 10. Conclusão

A Fase 2 representa a transição entre uma aplicação com infraestrutura própria e uma plataforma integrada ao ecossistema do Mercado Livre.

Sua implementação estabelecerá a base operacional necessária para as funcionalidades analíticas e de Inteligência Artificial previstas nas próximas fases.

---

**Documento:** 08_ROADMAP_FASE_02.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026