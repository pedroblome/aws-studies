# Lab 03 — RDS Database in a Private VPC

## What is it?

In this lab, you will learn how to deploy an Amazon RDS database in a VPC with the correct subnet architecture — the database in a private subnet (no direct internet access) and the application in a public or private subnet. This is the recommended security configuration for production databases.

## Use cases

- Web application databases in production
- Systems that need separation between the application and data layers
- Environments requiring security compliance (PCI DSS, GDPR)
- Any application with sensitive data requiring network isolation

## Key points for the exam (CLF-C02)

- **Never place a database in a public subnet** — this is a serious security flaw
- **DB Subnet Group**: required by RDS — defines which subnets the database can be created in (minimum 2 AZs for Multi-AZ)
- **RDS Security Group**: accepts connections only from the application layer's Security Group — on the database port (3306 for MySQL, 5432 for PostgreSQL)
- **Multi-AZ**: creates a standby replica in another AZ for automatic failover — recommended for production
- **Automatic backups**: enabled by default, 7-day retention — configurable up to 35 days
- **Access via Bastion Host**: to access the database via command line, use a Bastion Host in a public subnet as an intermediary
- **Parameter Groups**: database configurations managed by AWS — no OS-level access to the instance
- **Encryption at rest**: enable at creation time using KMS — cannot be enabled afterwards without recreating the database

## Practical example

**Conceptual scenario — Complete Architecture:**

**VPC structure (CIDR: 10.0.0.0/16):**
- Public subnet AZ-A: `10.0.1.0/24` → Bastion Host + NAT Gateway
- Public subnet AZ-B: `10.0.2.0/24` → (NAT Gateway backup)
- Private App subnet AZ-A: `10.0.11.0/24` → EC2 application instances
- Private App subnet AZ-B: `10.0.12.0/24` → EC2 application instances
- Private DB subnet AZ-A: `10.0.21.0/24` → RDS Primary
- Private DB subnet AZ-B: `10.0.22.0/24` → RDS Standby (Multi-AZ)

**Security Groups:**
- `sg-bastion`: accepts SSH (port 22) only from the office IP
- `sg-app`: accepts HTTP (port 8080) from the Load Balancer; can access `sg-db`
- `sg-db`: accepts MySQL (port 3306) ONLY from `sg-app` — completely isolated from the internet

**Access flow:**
- User → Internet Gateway → Load Balancer → EC2 (sg-app) → RDS (sg-db)
- DBA → Bastion Host (SSH) → EC2 → RDS (for maintenance)
- The database is NEVER directly accessible from the internet — maximum security.
