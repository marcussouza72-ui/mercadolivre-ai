# MercadoLivre AI SaaS

# 05 - Autenticação e Segurança

**Versão:** 1.0.0

**Fase:** Foundation

---

# 1. Objetivo

Este documento descreve a arquitetura de autenticação e segurança implementada na Fase 1 do MercadoLivre AI SaaS.

O objetivo é documentar os mecanismos de autenticação, autorização, proteção de credenciais e gerenciamento de tokens adotados pela aplicação.

---

# 2. Princípios de Segurança

A arquitetura foi construída seguindo os seguintes princípios:

- Nunca armazenar senhas em texto puro.
- Utilizar algoritmos modernos para hash de senhas.
- Separar autenticação de autorização.
- Utilizar tokens com tempo de expiração.
- Permitir renovação segura da sessão.
- Minimizar exposição de informações sensíveis.

---

# 3. Hash de Senhas

As senhas dos usuários são protegidas utilizando o algoritmo Argon2 por meio da biblioteca `pwdlib`.

### Benefícios

- Algoritmo recomendado para novas aplicações.
- Resistente a ataques de força bruta.
- Proteção contra ataques com GPU.
- Configuração segura por padrão.

Fluxo:

```text
Senha

↓

Argon2

↓

Hash

↓

Banco de Dados
```

Em nenhum momento a senha original é armazenada no banco de dados.

---

# 4. Autenticação

O processo de autenticação ocorre durante o login.

Fluxo:

```text
Cliente

↓

POST /auth/login

↓

Validação do e-mail

↓

Validação da senha

↓

Geração dos Tokens

↓

Resposta ao cliente
```

Após a autenticação bem-sucedida, são emitidos dois tokens:

- Access Token
- Refresh Token

---

# 5. JWT (JSON Web Token)

O sistema utiliza JWT para autenticação stateless.

Cada token é assinado digitalmente e contém informações necessárias para identificar o usuário.

Benefícios:

- Não exige armazenamento de sessão no servidor.
- Escalabilidade.
- Baixa latência.
- Facilidade de integração com APIs.

---

# 6. Access Token

O Access Token é utilizado para autenticar as requisições da API.

Características:

- Vida útil curta.
- Enviado no cabeçalho Authorization.
- Utilizado para acesso aos endpoints protegidos.

Formato:

```text
Authorization: Bearer <access_token>
```

---

# 7. Refresh Token

O Refresh Token possui a função de renovar a sessão do usuário sem exigir um novo login.

Características:

- Vida útil maior que o Access Token.
- Utilizado exclusivamente para renovação.
- Nunca deve ser utilizado para acessar endpoints protegidos.

---

# 8. Refresh Token Rotation

A aplicação implementa Refresh Token Rotation.

Fluxo:

```text
Login

↓

Access Token

+

Refresh Token

↓

Cliente

↓

POST /auth/refresh

↓

Validação do Refresh Token

↓

Novo Access Token

+

Novo Refresh Token

↓

Refresh anterior deixa de ser utilizado pelo cliente
```

Essa estratégia reduz riscos associados ao uso prolongado de um mesmo token.

---

# 9. Usuário Autenticado

Os endpoints protegidos utilizam uma dependência responsável por:

- validar o Access Token;
- identificar o usuário;
- carregar seus dados;
- disponibilizar o usuário autenticado para a camada de serviço.

Essa abordagem evita duplicação de lógica de autenticação.

---

# 10. Fluxo Geral de Segurança

```text
Cadastro

↓

Hash Argon2

↓

Banco de Dados

↓

Login

↓

JWT

↓

Access Token

+

Refresh Token

↓

Requisições autenticadas

↓

Expiração do Access Token

↓

POST /auth/refresh

↓

Novos Tokens
```

---

# 11. Endpoints Implementados

Durante a Fase 1 foram implementados os seguintes endpoints relacionados à autenticação:

| Método | Endpoint | Finalidade |
|---------|----------|------------|
| POST | /auth/register | Cadastro de usuário |
| POST | /auth/login | Autenticação |
| POST | /auth/refresh | Renovação dos tokens |
| GET | /auth/me | Retorna o usuário autenticado |

---

# 12. Próximas Evoluções

Na Fase 2, a arquitetura de autenticação será expandida para suportar:

- OAuth 2.0 do Mercado Livre.
- Múltiplas contas por usuário.
- Gerenciamento de Access Token do Mercado Livre.
- Renovação automática dos tokens OAuth.
- Revogação de sessões.
- Auditoria de autenticação.

---

# 13. Conclusão

A arquitetura implementada fornece um mecanismo de autenticação moderno, seguro e escalável.

A combinação de Argon2, JWT e Refresh Token Rotation estabelece uma base sólida para as futuras integrações da plataforma, mantendo a separação entre autenticação da aplicação e autenticação de serviços externos.

---

**Documento:** 05_AUTENTICACAO_E_SEGURANCA.md

**Versão:** 1.0.0

**Última atualização:** Julho/2026