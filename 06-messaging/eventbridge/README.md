# Amazon EventBridge

## O que é?

Amazon EventBridge é um barramento de eventos serverless que facilita a construção de aplicações orientadas a eventos. Conecta diferentes aplicações usando eventos — recebe eventos de fontes AWS, parceiros SaaS ou aplicações customizadas e os roteita para targets como Lambda, SQS, SNS, Step Functions e muito mais.

## Casos de uso

- Orquestração de microsserviços baseada em eventos
- Automação de operações (ex: snapshots automáticos quando um EC2 é iniciado)
- Agendamento de tarefas (substituto moderno do CloudWatch Events para cron)
- Integração com aplicações SaaS (Datadog, Zendesk, Shopify) sem código intermediário
- Auditoria e roteamento de eventos de segurança (GuardDuty, Security Hub)

## Pontos-chave para a prova (CLF-C02)

- **Event Bus**: canal onde os eventos fluem — há um bus padrão (AWS events), buses de parceiros e buses customizados
- **Rules (Regras)**: filtram eventos com base em padrões e os roteiam para targets — você define "se o evento for X, envie para Y"
- **Targets**: onde o evento é enviado — Lambda, SQS, SNS, Step Functions, EC2, Kinesis, API Gateway, etc. (até 5 targets por regra)
- **Schema Registry**: catálogo de esquemas de eventos — facilita o desenvolvimento com autocompletar e validação
- **EventBridge Scheduler**: agenda tarefas em horários específicos ou em intervalos (ex: executar Lambda todo dia às 8h)
- **Diferença do SNS**: EventBridge tem roteamento baseado em conteúdo do evento e integra com 200+ fontes SaaS; SNS é mais simples e para notificações
- **Substituto do CloudWatch Events**: o CloudWatch Events foi renomeado para EventBridge — mesma funcionalidade, mais recursos
- **Serverless e gerenciado**: sem infraestrutura para gerenciar, escala automaticamente

## Exemplo prático

**Cenário:** Uma empresa quer automatizar ações de segurança. Quando o AWS GuardDuty detecta uma atividade suspeita, ele publica um evento no EventBridge. Uma regra filtra eventos com severidade alta e os envia simultaneamente para: (1) uma função Lambda que bloqueia automaticamente o IP suspeito no WAF, (2) uma fila SQS que notifica o time de segurança, (3) um registro no S3 para auditoria. Tudo automatizado sem intervenção humana.
