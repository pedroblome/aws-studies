# AWS Lambda

## O que é?

AWS Lambda é um serviço de computação **serverless** (sem servidor) que executa seu código em resposta a eventos, sem que você precise provisionar ou gerenciar servidores. Você paga apenas pelo tempo de execução do código — medido em milissegundos.

## Casos de uso

- APIs e backends serverless (integrado com API Gateway)
- Processamento de eventos em tempo real (uploads no S3, mensagens no SQS/SNS)
- Automação de tarefas e agendamento (similar ao cron, via EventBridge)
- Transformação e processamento de dados (ETL leve)
- Webhooks e integrações entre sistemas

## Pontos-chave para a prova (CLF-C02)

- **Serverless**: você não gerencia servidores — a AWS cuida de toda a infraestrutura
- **Event-driven**: o Lambda é acionado por eventos (HTTP via API Gateway, upload no S3, mensagem no SQS, etc.)
- **Precificação**: cobrança por número de requisições e duração da execução — primeiros 1 milhão de requisições/mês são gratuitas (free tier permanente)
- **Tempo máximo de execução**: 15 minutos por invocação
- **Linguagens suportadas**: Python, Node.js, Java, Go, Ruby, C#, e runtimes customizados
- **Escala automaticamente**: de zero a milhares de execuções simultâneas sem configuração
- **Lambda é FaaS** (Function as a Service) — o menor nível de abstração no modelo serverless
- Integra-se nativamente com dezenas de serviços AWS

## Exemplo prático

**Cenário:** Um e-commerce precisa redimensionar automaticamente imagens enviadas por usuários. Quando um usuário faz upload de uma foto para um bucket S3, um evento aciona uma função Lambda que processa a imagem (redimensiona, comprime), salva a versão otimizada em outro bucket S3 e registra o resultado no DynamoDB. Tudo sem servidores — o time não precisa gerenciar nenhuma infraestrutura.
