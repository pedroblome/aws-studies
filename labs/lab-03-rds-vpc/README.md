# Lab 03 — Banco de Dados RDS em VPC Privada

## O que é?

Neste laboratório, você aprenderá a implantar um banco de dados Amazon RDS em uma VPC com arquitetura de sub-redes correta — o banco de dados em sub-rede privada (sem acesso direto à internet) e a aplicação em sub-rede pública ou privada. Esta é a configuração de segurança recomendada para bancos de dados em produção.

## Casos de uso

- Bancos de dados de aplicações web em produção
- Sistemas que precisam de separação entre camada de aplicação e dados
- Ambientes que exigem conformidade de segurança (PCI DSS, LGPD)
- Qualquer aplicação com dados sensíveis que requerem isolamento de rede

## Pontos-chave para a prova (CLF-C02)

- **Nunca coloque um banco de dados em sub-rede pública** — é uma falha grave de segurança
- **DB Subnet Group**: requisito do RDS — define em quais sub-redes o banco pode ser criado (mínimo 2 AZs para Multi-AZ)
- **Security Group do RDS**: aceita conexões apenas do Security Group da camada de aplicação — na porta do banco (3306 para MySQL, 5432 para PostgreSQL)
- **Multi-AZ**: cria uma réplica standby em outra AZ para failover automático — recomendado para produção
- **Backups automáticos**: habilitados por padrão, retenção de 7 dias — configurável até 35 dias
- **Acesso via Bastion Host**: para acessar o banco via linha de comando, use um Bastion Host em sub-rede pública como intermediário
- **Parameter Groups**: configurações do banco de dados gerenciadas pela AWS — sem acesso ao SO da instância
- **Encryption at rest**: habilite na criação usando KMS — não pode ser habilitado depois sem recriar o banco

## Exemplo prático

**Cenário conceitual — Arquitetura Completa:**

**Estrutura da VPC (CIDR: 10.0.0.0/16):**
- Sub-rede pública AZ-A: `10.0.1.0/24` → Bastion Host + NAT Gateway
- Sub-rede pública AZ-B: `10.0.2.0/24` → (backup do NAT Gateway)
- Sub-rede privada App AZ-A: `10.0.11.0/24` → Instâncias EC2 da aplicação
- Sub-rede privada App AZ-B: `10.0.12.0/24` → Instâncias EC2 da aplicação
- Sub-rede privada DB AZ-A: `10.0.21.0/24` → RDS Primary
- Sub-rede privada DB AZ-B: `10.0.22.0/24` → RDS Standby (Multi-AZ)

**Security Groups:**
- `sg-bastion`: aceita SSH (porta 22) apenas do IP do escritório
- `sg-app`: aceita HTTP (porta 8080) do Load Balancer; pode acessar `sg-db`
- `sg-db`: aceita MySQL (porta 3306) APENAS de `sg-app` — completamente isolado da internet

**Fluxo de acesso:**
- Usuário → Internet Gateway → Load Balancer → EC2 (sg-app) → RDS (sg-db)
- DBA → Bastion Host (SSH) → EC2 → RDS (para manutenção)
- O banco de dados JAMAIS é acessível diretamente pela internet — máxima segurança.
