# Amazon SQS (Simple Queue Service)

## O que é?

Amazon SQS é um serviço de fila de mensagens totalmente gerenciado que permite desacoplar e escalar microsserviços, sistemas distribuídos e aplicações serverless. Permite que um componente envie mensagens para a fila sem precisar que o destinatário esteja disponível no momento do envio.

## Casos de uso

- Desacoplar componentes de uma aplicação (produtor e consumidor independentes)
- Processar tarefas em background (envio de e-mails, geração de relatórios, processamento de imagens)
- Absorver picos de tráfego — a fila funciona como um buffer
- Garantir que nenhuma mensagem seja perdida mesmo se o consumidor estiver offline
- Comunicação entre microsserviços de forma assíncrona

## Pontos-chave para a prova (CLF-C02)

- **Tipos de fila:**
  - **Standard Queue**: alta vazão, entrega pelo menos uma vez (at-least-once), ordem não garantida — para a maioria dos casos
  - **FIFO Queue**: entrega exatamente uma vez (exactly-once), ordem garantida, menor vazão (300 msgs/s) — para processos que exigem ordem
- **Retention Period**: mensagens ficam na fila de 1 minuto a 14 dias (padrão: 4 dias)
- **Visibility Timeout**: após o consumidor receber a mensagem, ela fica invisível por um período — se não for deletada, volta à fila
- **Dead Letter Queue (DLQ)**: fila separada para mensagens que falharam múltiplas vezes — facilita debugging
- **Long Polling**: o consumidor aguarda até que uma mensagem esteja disponível (reduz chamadas vazias e custos)
- **Tamanho máximo de mensagem**: 256 KB (use S3 + SQS para mensagens maiores)
- **SQS vs SNS**: SQS = pull (consumidor busca mensagens); SNS = push (mensagens enviadas para assinantes)

## Exemplo prático

**Cenário:** Um e-commerce processa pedidos em alta velocidade. Em vez de o servidor web processar o pagamento sincronamente (e deixar o usuário esperando), ele envia o pedido para uma fila SQS e responde imediatamente ao usuário. Um conjunto de workers Lambda consome a fila e processa os pagamentos de forma assíncrona. Durante a Black Friday, a fila absorve 100 mil pedidos sem sobrecarregar o sistema de pagamento — os pedidos são processados na velocidade que o sistema suporta.
