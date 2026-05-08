# AWS Elastic Beanstalk

## O que é?

AWS Elastic Beanstalk é um serviço de **PaaS (Platform as a Service)** que facilita o deploy e gerenciamento de aplicações web. Você faz upload do código e o Beanstalk cuida automaticamente do provisionamento de capacidade, balanceamento de carga, escalabilidade e monitoramento — sem necessidade de gerenciar a infraestrutura diretamente.

## Casos de uso

- Deploy rápido de aplicações web para times que não querem gerenciar infraestrutura
- Ambientes de desenvolvimento e homologação ágeis
- Migração de aplicações on-premises para a nuvem com mínimas mudanças
- Startups que querem focar no produto, não na infra
- Aplicações em linguagens como Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker

## Pontos-chave para a prova (CLF-C02)

- **PaaS**: você gerencia apenas o código e as configurações da aplicação — a AWS gerencia o resto
- O Beanstalk é **gratuito** — você paga apenas pelos recursos subjacentes que ele provisiona (EC2, RDS, ELB, etc.)
- Suporta múltiplos ambientes (produção, staging) com deploys isolados
- Mantém o **controle total** sobre os recursos — diferente de Lambda, você ainda pode acessar as instâncias EC2
- Gerencia automaticamente: provisionamento de EC2, configuração do Load Balancer, Auto Scaling, monitoramento via CloudWatch
- Ideal para **deploys rápidos** sem expertise em infraestrutura AWS
- **Não recomendado** para arquiteturas muito customizadas — nesses casos, gerenciar EC2/ECS diretamente é melhor

## Exemplo prático

**Cenário:** Uma agência de desenvolvimento precisa entregar rapidamente uma aplicação Node.js para um cliente. Usando o Elastic Beanstalk, o dev faz upload do código via CLI (`eb deploy`). O Beanstalk cria automaticamente as instâncias EC2, configura o Nginx, habilita o Auto Scaling e o Load Balancer, e disponibiliza a aplicação em uma URL pública — tudo em menos de 10 minutos, sem que o desenvolvedor precise conhecer os detalhes da infraestrutura AWS.
