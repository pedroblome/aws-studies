# Amazon RDS (Relational Database Service)

## O que é?

Amazon RDS é um serviço de banco de dados relacional gerenciado que facilita a configuração, operação e escalabilidade de bancos de dados na nuvem. A AWS gerencia tarefas administrativas como provisionamento de hardware, instalação do banco, patches, backups e recuperação — você foca na sua aplicação.

## Casos de uso

- Bancos de dados para aplicações web e mobile (e-commerce, SaaS, CRMs)
- Migração de bancos de dados on-premises para a nuvem
- Aplicações que requerem transações ACID e joins complexos
- Sistemas financeiros e contábeis com dados relacionais
- Backends de aplicações que usam ORM (Hibernate, ActiveRecord, etc.)

## Pontos-chave para a prova (CLF-C02)

- **Bancos suportados**: MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server, e Amazon Aurora
- **Multi-AZ**: replica os dados sincronamente para uma instância standby em outra AZ — failover automático em caso de falha (alta disponibilidade)
- **Read Replicas**: cópias assíncronas do banco para distribuir carga de leitura — melhoram a performance (não são para failover)
- **Backups automáticos**: retenção de 1 a 35 dias, com restauração para qualquer ponto no tempo (PITR)
- **Gerenciado pela AWS**: patches do SO e do banco, backups, monitoramento — você não tem acesso SSH à instância
- **RDS é diferente do DynamoDB**: RDS = relacional (SQL); DynamoDB = NoSQL (chave-valor/documento)
- **Encryption at rest**: suporte a criptografia com KMS — deve ser habilitada na criação
- **Security Groups** controlam o acesso à instância RDS

## Exemplo prático

**Cenário:** Uma startup tem um banco de dados MySQL em um servidor dedicado que requer manutenção constante. Ao migrar para o Amazon RDS for MySQL com Multi-AZ, a AWS passa a gerenciar backups diários, aplicar patches de segurança automaticamente e fazer failover em menos de 2 minutos se a instância principal falhar. O time de dev para de se preocupar com DBA e foca no produto. Read Replicas são adicionadas para os relatórios pesados, sem impactar a performance da produção.
