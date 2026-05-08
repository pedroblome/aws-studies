# Amazon EC2 (Elastic Compute Cloud)

## O que é?

Amazon EC2 é o serviço de computação virtual da AWS que fornece servidores (instâncias) na nuvem. Você escolhe o tipo de instância (CPU, memória, armazenamento), o sistema operacional e paga apenas pelo tempo de uso. É a base da infraestrutura de computação da AWS.

## Casos de uso

- Hospedar aplicações web e APIs backend
- Executar servidores de banco de dados
- Processar grandes volumes de dados (big data, machine learning)
- Ambiente de desenvolvimento e testes
- Hospedar aplicações legadas que requerem controle total do servidor

## Pontos-chave para a prova (CLF-C02)

- **Modelos de precificação:**
  - **On-Demand**: pague pelo que usar, sem compromisso — ideal para cargas imprevisíveis
  - **Reserved Instances**: desconto de até 72% com compromisso de 1 ou 3 anos
  - **Spot Instances**: até 90% mais barato, mas a AWS pode interromper — ideal para cargas tolerantes a falhas
  - **Savings Plans**: desconto similar ao Reserved, com mais flexibilidade de uso
  - **Dedicated Hosts**: servidor físico dedicado — para conformidade ou licenças de software
- **Tipos de instância:** General Purpose (T, M), Compute Optimized (C), Memory Optimized (R, X), Storage Optimized (I, D)
- **EC2 é um serviço IaaS** (Infrastructure as a Service) — você gerencia o SO e acima
- **Auto Scaling** escala automaticamente a quantidade de instâncias conforme a demanda
- **Elastic Load Balancer (ELB)** distribui o tráfego entre múltiplas instâncias
- **Security Groups** funcionam como firewall virtual no nível da instância

## Exemplo prático

**Cenário:** Uma loja virtual tem picos de tráfego durante a Black Friday. O arquiteto configura um Auto Scaling Group com instâncias EC2 do tipo `t3.medium` (On-Demand para o mínimo) e Spot Instances para absorver os picos — economizando até 70% nos custos extras. Um Application Load Balancer distribui as requisições entre as instâncias, e o CloudWatch monitora a CPU para acionar o scaling automaticamente.
