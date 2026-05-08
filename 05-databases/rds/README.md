# Amazon RDS (Relational Database Service)

## What is it?

Amazon RDS is a managed relational database service that makes it easy to set up, operate, and scale databases in the cloud. AWS handles administrative tasks such as hardware provisioning, database installation, patching, backups, and recovery — you focus on your application.

## Use cases

- Databases for web and mobile applications (e-commerce, SaaS, CRMs)
- Migrating on-premises databases to the cloud
- Applications requiring ACID transactions and complex joins
- Financial and accounting systems with relational data
- Application backends using ORMs (Hibernate, ActiveRecord, etc.)

## Key points for the exam (CLF-C02)

- **Supported databases**: MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server, and Amazon Aurora
- **Multi-AZ**: synchronously replicates data to a standby instance in another AZ — automatic failover in the event of a failure (high availability)
- **Read Replicas**: asynchronous copies of the database to distribute read load — improve performance (not for failover)
- **Automatic backups**: retention from 1 to 35 days, with point-in-time restore (PITR)
- **Managed by AWS**: OS and database patching, backups, monitoring — you do not have SSH access to the instance
- **RDS differs from DynamoDB**: RDS = relational (SQL); DynamoDB = NoSQL (key-value/document)
- **Encryption at rest**: KMS encryption support — must be enabled at creation time
- **Security Groups** control access to the RDS instance

## Practical example

**Scenario:** A startup has a MySQL database on a dedicated server requiring constant maintenance. By migrating to Amazon RDS for MySQL with Multi-AZ, AWS takes over daily backups, automatically applies security patches, and performs failover in under 2 minutes if the primary instance fails. The dev team stops worrying about DBA tasks and focuses on the product. Read Replicas are added for heavy reporting queries without impacting production performance.
