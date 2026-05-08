# Padrões de Arquitetura Serverless

## O que é?

Arquitetura serverless é um modelo de computação em nuvem onde o provedor gerencia toda a infraestrutura de servidor — o desenvolvedor foca apenas no código. Na AWS, serverless não significa "sem servidores", mas sim que você não gerencia servidores. Os padrões serverless são combinações de serviços AWS que resolvem problemas comuns sem provisionamento de infraestrutura.

## Casos de uso

- APIs REST e backends para aplicações mobile e web
- Processamento de eventos em tempo real (uploads, mensagens, streams)
- Automação e orquestração de workflows
- Chatbots e assistentes virtuais
- Processamento de dados em batch sem servidores
- Webhooks e integrações entre sistemas

## Pontos-chave para a prova (CLF-C02)

**Serviços serverless principais na AWS:**
- **Computação**: AWS Lambda
- **API**: Amazon API Gateway
- **Banco de dados**: Amazon DynamoDB, Aurora Serverless
- **Armazenamento**: Amazon S3
- **Mensageria**: Amazon SQS, SNS, EventBridge
- **Orquestração**: AWS Step Functions
- **Autenticação**: Amazon Cognito

**Padrões arquiteturais comuns:**

1. **API Serverless**: API Gateway → Lambda → DynamoDB
2. **Event Processing**: S3 Upload → Lambda → processamento → S3/DynamoDB
3. **Fan-out**: SNS → múltiplos SQS → múltiplos Lambda (processamento paralelo)
4. **Workflow**: Step Functions orquestran múltiplos Lambda em sequência com lógica de negócio
5. **Scheduled Jobs**: EventBridge Scheduler → Lambda (substituto serverless do cron)

**Vantagens do serverless:**
- **Sem gerenciamento de servidor**: foco total no código de negócio
- **Escala automática**: de zero a milhões de requisições sem configuração
- **Pay-per-use**: pague apenas pelo que usar — zero custo quando não há tráfego
- **Alta disponibilidade**: built-in por padrão nos serviços gerenciados

## Exemplo prático

**Cenário:** Um aplicativo de delivery precisa processar pedidos em tempo real. Arquitetura serverless: o app mobile chama uma API REST (API Gateway) → Lambda valida o pedido e salva no DynamoDB → DynamoDB Streams aciona outro Lambda → que publica no SNS → que fan-out para: (1) Lambda notifica o restaurante via SMS (SNS); (2) SQS enfileira para o sistema de rastreamento. Step Functions orquestra o fluxo de estados do pedido (recebido → preparando → saiu para entrega → entregue). Zero servidores — escala para 100 mil pedidos simultâneos automaticamente.
