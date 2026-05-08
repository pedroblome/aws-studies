# AWS X-Ray

## O que é?

AWS X-Ray é um serviço de rastreamento distribuído que ajuda a analisar e depurar aplicações em produção, especialmente arquiteturas distribuídas e microsserviços. Permite visualizar o fluxo completo de uma requisição através de múltiplos serviços, identificando gargalos e erros.

## Casos de uso

- Depurar problemas de performance em aplicações com microsserviços
- Identificar gargalos e latências em arquiteturas distribuídas
- Rastrear requisições end-to-end em aplicações serverless (Lambda + API Gateway)
- Analisar erros e exceções em produção com contexto completo
- Entender como os serviços se comunicam e onde ocorrem falhas

## Pontos-chave para a prova (CLF-C02)

- **Distributed Tracing**: rastreia uma requisição através de múltiplos serviços, criando um mapa visual do fluxo
- **Service Map**: visualização gráfica de todos os serviços e como eles se conectam — identifica rapidamente onde ocorrem erros ou lentidões
- **Traces e Segments**: um trace é o caminho completo de uma requisição; cada serviço adiciona um segment ao trace
- **SDK X-Ray**: instrumentação via SDK na aplicação (disponível para Python, Java, Node.js, .NET, Go, Ruby)
- **X-Ray Daemon**: processo que coleta e envia os dados de rastreamento para o serviço X-Ray
- Integra-se nativamente com: **Lambda, API Gateway, ECS, EC2, Elastic Beanstalk, SNS, SQS**
- **Sampling**: X-Ray não rastreia 100% das requisições por padrão — usa amostragem para reduzir custos e overhead
- **Annotations e Metadata**: adicione informações customizadas aos traces para facilitar a análise

## Exemplo prático

**Cenário:** Um microsserviço de checkout está lento — os usuários reclamam de demora no pagamento. Com X-Ray instrumentado na aplicação, o time abre o Service Map e visualiza o fluxo: API Gateway → Lambda (checkout) → RDS (verificação de estoque) → serviço de pagamento externo. O X-Ray mostra que a chamada ao RDS leva 2,8 segundos — muito acima do normal. O time identifica uma query sem índice e resolve o problema, reduzindo o tempo total de 3,5 segundos para 180ms.
