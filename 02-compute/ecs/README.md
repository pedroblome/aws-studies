# Amazon ECS (Elastic Container Service)

## O que é?

Amazon ECS é um serviço de orquestração de contêineres totalmente gerenciado que permite executar, escalar e gerenciar aplicações em contêineres Docker na AWS. O ECS elimina a necessidade de instalar e operar sua própria infraestrutura de orquestração de contêineres.

## Casos de uso

- Executar microsserviços em contêineres Docker
- Migração de aplicações monolíticas para arquitetura de microsserviços
- Pipelines de CI/CD que deployam imagens de contêiner
- Processamento em lote com contêineres
- Aplicações web altamente escaláveis em contêineres

## Pontos-chave para a prova (CLF-C02)

- **Dois modos de execução (launch types):**
  - **EC2 Launch Type**: você gerencia as instâncias EC2 que hospedam os contêineres
  - **Fargate Launch Type**: **serverless** — a AWS gerencia a infraestrutura subjacente, você só define CPU/memória para o contêiner
- **Integra-se nativamente** com ECR (repositório de imagens), Load Balancer, IAM, CloudWatch
- **Task Definition**: define como um contêiner deve ser executado (imagem, CPU, memória, variáveis de ambiente)
- **Service**: garante que um número específico de tasks esteja sempre rodando
- **ECS vs EKS**: ECS é mais simples e integrado à AWS; EKS usa Kubernetes e é mais complexo mas mais portável
- Fargate é a opção **serverless** para contêineres — elimina o gerenciamento de servidores

## Exemplo prático

**Cenário:** Uma fintech tem uma API REST empacotada em Docker. Com ECS + Fargate, o time faz deploy da imagem do ECR sem se preocupar com servidores. Um Application Load Balancer distribui o tráfego, e o ECS Service garante que sempre haja 3 tasks rodando. Quando o CloudWatch detecta aumento de CPU, o ECS Auto Scaling sobe novas tasks automaticamente — tudo sem gerenciar nenhuma instância EC2.
