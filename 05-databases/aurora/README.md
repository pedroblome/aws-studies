# Amazon Aurora

## O que é?

Amazon Aurora é um banco de dados relacional desenvolvido pela AWS, compatível com MySQL e PostgreSQL, que combina a performance e disponibilidade de bancos comerciais de alto padrão com a simplicidade e custo de bancos de código aberto. Aurora é parte do Amazon RDS.

## Casos de uso

- Aplicações de missão crítica que exigem alta disponibilidade e performance
- Migração de Oracle ou SQL Server para um banco open-source de alto desempenho
- Aplicações SaaS multi-tenant que precisam escalar
- Workloads de leitura intensiva com múltiplas réplicas
- Aplicações globais com Aurora Global Database

## Pontos-chave para a prova (CLF-C02)

- **5x mais rápido que MySQL padrão** e **3x mais rápido que PostgreSQL padrão**
- **Armazenamento distribuído e auto-reparável**: dados replicados 6 vezes em 3 AZs automaticamente
- **Auto scaling de armazenamento**: começa com 10 GB e escala automaticamente em incrementos de 10 GB até 128 TB
- **Alta disponibilidade nativa**: até 15 Read Replicas (RDS suporta até 5); failover em menos de 30 segundos
- **Aurora Serverless**: capacidade computacional escala automaticamente com base na demanda — ideal para cargas imprevisíveis
- **Aurora Global Database**: replica os dados para até 5 regiões secundárias com latência de menos de 1 segundo — para DR e leituras globais
- **Compatível com MySQL e PostgreSQL**: mudança mínima de código ao migrar
- **Mais caro que RDS padrão**, mas mais barato que bancos de dados comerciais (Oracle, SQL Server)
- Gerenciado como parte do RDS — mesmas interfaces de gerenciamento

## Exemplo prático

**Cenário:** Uma plataforma de pagamentos processa 50 mil transações por segundo durante picos de vendas. O MySQL on-premises não aguentava a carga. Com Aurora MySQL com Multi-Master, múltiplos nodes podem aceitar escritas simultaneamente. Aurora Global Database replica os dados para a região de backup em menos de 1 segundo. Se a região primária falhar, o failover para a região secundária é feito em menos de 1 minuto — SLA de 99,99% de disponibilidade atendido.
