# Alta Disponibilidade (High Availability)

## O que é?

Alta Disponibilidade (HA) é a capacidade de um sistema de permanecer operacional e acessível por um longo período, mesmo diante de falhas de componentes individuais. Na AWS, HA é alcançada através da distribuição de recursos em múltiplas Zonas de Disponibilidade (AZs) e regiões, com failover automático.

## Casos de uso

- Aplicações críticas de negócio que não podem ter downtime (banking, e-commerce, saúde)
- Sistemas que precisam de SLA de 99,99% ou superior
- Proteção contra falhas de datacenter e manutenções planejadas
- Recuperação automática de desastres (Disaster Recovery)
- Ambientes de produção com milhões de usuários

## Pontos-chave para a prova (CLF-C02)

**Conceitos fundamentais:**

- **Alta Disponibilidade vs Tolerância a Falhas:**
  - HA = o sistema continua operacional após uma falha (pode haver breve interrupção)
  - Fault Tolerance = o sistema opera SEM NENHUMA interrupção mesmo durante falhas (mais caro e complexo)

- **Região vs Zona de Disponibilidade:**
  - Região: área geográfica com múltiplos datacenters (ex: sa-east-1 = São Paulo)
  - AZ (Zona de Disponibilidade): datacenter(s) isolados dentro de uma região — conectados por fibra de baixa latência

**Padrões de HA na AWS:**

1. **Multi-AZ**: distribuir recursos (EC2, RDS, ElastiCache) em 2+ AZs com failover automático
2. **Auto Scaling**: substituir automaticamente instâncias com falha por novas instâncias saudáveis
3. **Elastic Load Balancer**: distribuir tráfego entre instâncias saudáveis em múltiplas AZs
4. **RDS Multi-AZ**: réplica síncrona em standby — failover automático em menos de 2 minutos
5. **Route 53 Health Checks + Failover**: redirecionar tráfego para região de backup se a principal falhar

**SLAs de disponibilidade:**
- 99,9% = 8,7 horas de downtime/ano
- 99,99% = 52 minutos de downtime/ano
- 99,999% = 5 minutos de downtime/ano (five nines)

## Exemplo prático

**Cenário:** Um banco projeta sua aplicação web para 99,99% de disponibilidade. A arquitetura usa: ALB distribuindo tráfego entre EC2 em 2 AZs (us-east-1a e us-east-1b) com Auto Scaling Group mínimo de 2 instâncias; RDS Aurora com Multi-AZ e failover automático; ElastiCache Redis em cluster multi-AZ; Route 53 com health checks e failover para uma região secundária (us-west-2). Quando a AZ us-east-1a vai abaixo para manutenção, o tráfego é automaticamente redirecionado para us-east-1b — sem nenhum usuário perceber.
