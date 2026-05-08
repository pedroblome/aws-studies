# Lab 02 — API REST Serverless com Lambda e API Gateway

## O que é?

Neste laboratório, você aprenderá a construir uma API REST completamente serverless usando Amazon API Gateway como frontend HTTP e AWS Lambda como backend de processamento, com dados armazenados no DynamoDB. Esta é a arquitetura serverless mais comum e amplamente usada na AWS.

## Casos de uso

- Backends para aplicativos mobile e web
- Microsserviços serverless
- APIs de integração entre sistemas
- Processamento de webhooks
- APIs com tráfego variável (pague apenas pelo uso)

## Pontos-chave para a prova (CLF-C02)

- **API Gateway + Lambda**: a combinação padrão para APIs serverless na AWS
- **API Gateway**: gerencia autenticação, throttling, caching, documentação e roteamento de requisições
- **Lambda**: processa as requisições sem servidor — escala de 0 a milhares de invocações simultâneas
- **DynamoDB**: banco NoSQL serverless — complemento natural ao Lambda para armazenar dados
- **Sem servidor para gerenciar**: toda a infraestrutura é gerenciada pela AWS
- **Pay-per-use**: pague por requisição no API Gateway e por milissegundo de execução no Lambda
- **IAM + API Keys + Cognito**: opções para autenticar e autorizar chamadas à API
- **CORS**: deve ser habilitado no API Gateway para chamadas de browsers
- **Stages**: ambientes de deploy no API Gateway (dev, staging, prod) com URLs separadas

## Exemplo prático

**Cenário conceitual — API de Tarefas (To-Do List):**

**Endpoints da API:**
- `POST /tasks` → Lambda cria nova tarefa no DynamoDB
- `GET /tasks` → Lambda lista todas as tarefas do DynamoDB
- `GET /tasks/{id}` → Lambda busca tarefa por ID
- `PUT /tasks/{id}` → Lambda atualiza tarefa
- `DELETE /tasks/{id}` → Lambda deleta tarefa

**Fluxo de uma requisição:**
1. App mobile envia `POST /tasks` com `{"title": "Estudar AWS"}` para o API Gateway
2. API Gateway autentica a requisição via API Key e valida o JSON
3. API Gateway invoca a função Lambda `CreateTask`
4. Lambda recebe o evento, gera um UUID, salva `{"id": "abc123", "title": "Estudar AWS", "done": false}` no DynamoDB
5. Lambda retorna `{"statusCode": 201, "body": {"id": "abc123"}}`
6. API Gateway retorna a resposta ao app com status HTTP 201

**Custo para 1 milhão de requisições/mês**: aproximadamente $3.50 (API Gateway) + $0.20 (Lambda) + custo mínimo do DynamoDB = menos de $5/mês total, com **zero** servidores para gerenciar.
