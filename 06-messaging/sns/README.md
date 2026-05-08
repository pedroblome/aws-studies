# Amazon SNS (Simple Notification Service)

## O que é?

Amazon SNS é um serviço de mensagens pub/sub (publicação/assinatura) totalmente gerenciado que permite enviar notificações para múltiplos destinatários simultaneamente. Um produtor publica uma mensagem em um **tópico** e o SNS entrega essa mensagem a todos os **assinantes** daquele tópico.

## Casos de uso

- Notificações push para aplicativos mobile (iOS, Android)
- Envio de alertas via e-mail e SMS para equipes de operações
- Fan-out: disparar múltiplas ações em paralelo a partir de um evento
- Notificações em tempo real para usuários
- Integração com SQS para arquitetura fan-out (SNS → múltiplas filas SQS)

## Pontos-chave para a prova (CLF-C02)

- **Modelo Pub/Sub**: publicadores enviam para tópicos; assinantes (subscribers) recebem automaticamente
- **Protocolos de entrega**: HTTP/HTTPS, e-mail, e-mail JSON, SMS, SQS, Lambda, aplicações mobile (push)
- **Fan-out pattern**: uma mensagem publicada em um tópico SNS é entregue simultaneamente a múltiplas filas SQS — padrão clássico para processamento paralelo
- **Push-based**: o SNS empurra mensagens para os assinantes (diferente do SQS onde o consumidor puxa)
- **SNS FIFO**: tópicos com entrega ordenada e sem duplicatas — para casos que exigem ordem
- **Message Filtering**: assinantes podem filtrar quais mensagens receber com base em atributos — evita processar mensagens irrelevantes
- **Sem retenção**: o SNS não armazena mensagens — se um assinante não estiver disponível, a mensagem é perdida (use SQS para garantir entrega)
- Limite de **12,5 milhões de assinaturas** por tópico

## Exemplo prático

**Cenário:** Um sistema de monitoramento de infraestrutura detecta que um servidor está com CPU acima de 90%. Um alarme do CloudWatch publica uma mensagem no tópico SNS `AlertasCriticos`. O SNS entrega simultaneamente: (1) um e-mail para o time de Ops, (2) um SMS para o plantão de suporte, (3) uma mensagem para uma fila SQS que aciona um Lambda para tentar remediar automaticamente o problema. Um único evento dispara três ações paralelas.
