# Amazon Aurora

## What is it?

Amazon Aurora is a relational database built by AWS, compatible with MySQL and PostgreSQL, that combines the performance and availability of high-end commercial databases with the simplicity and cost of open-source databases. Aurora is part of Amazon RDS.

## Use cases

- Mission-critical applications requiring high availability and performance
- Migrating from Oracle or SQL Server to a high-performance open-source database
- Multi-tenant SaaS applications that need to scale
- Read-intensive workloads with multiple replicas
- Global applications using Aurora Global Database

## Key points for the exam (CLF-C02)

- **5x faster than standard MySQL** and **3x faster than standard PostgreSQL**
- **Distributed, self-healing storage**: data replicated 6 times across 3 AZs automatically
- **Auto-scaling storage**: starts at 10 GB and scales automatically in 10 GB increments up to 128 TB
- **Native high availability**: up to 15 Read Replicas (RDS supports up to 5); failover in under 30 seconds
- **Aurora Serverless**: compute capacity scales automatically based on demand — ideal for unpredictable workloads
- **Aurora Global Database**: replicates data to up to 5 secondary regions with less than 1 second of latency — for DR and global reads
- **Compatible with MySQL and PostgreSQL**: minimal code changes when migrating
- **More expensive than standard RDS**, but cheaper than commercial databases (Oracle, SQL Server)
- Managed as part of RDS — same management interfaces

## Practical example

**Scenario:** A payments platform processes 50,000 transactions per second during peak sales. On-premises MySQL could not handle the load. With Aurora MySQL Multi-Master, multiple nodes can accept writes simultaneously. Aurora Global Database replicates data to the backup region in under 1 second. If the primary region fails, failover to the secondary region completes in under 1 minute — meeting a 99.99% availability SLA.
