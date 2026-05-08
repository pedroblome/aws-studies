# AWS Secrets Manager

## What is it?

AWS Secrets Manager is a service that helps protect access to applications, services, and IT resources. It allows you to securely store, rotate, manage, and retrieve database credentials, API keys, and other secrets — eliminating hardcoded secrets in source code.

## Use cases

- Store database credentials (username/password for RDS, Aurora, etc.)
- Manage API keys for external services (Stripe, Twilio, SendGrid)
- Rotate passwords automatically without changing application code
- Centralize secret management in multi-account environments
- Meet security policies that prohibit credentials in code or configuration files

## Key points for the exam (CLF-C02)

- **Automatic rotation**: Secrets Manager can automatically rotate secrets on defined intervals — with no application downtime
- **Native integration with RDS, Aurora, Redshift, DocumentDB**: automatic database password rotation configurable in a few clicks
- **Encryption**: all secrets are encrypted with KMS
- **Versioning**: keeps previous versions of the secret for rollback
- **Secrets Manager vs SSM Parameter Store:**
  - Secrets Manager: focused on secrets, automatic rotation, cost per secret (~$0.40/month)
  - SSM Parameter Store: more general (configs + secrets), cheaper, no native automatic rotation for databases
- **SDK integration**: applications call Secrets Manager via SDK instead of reading configuration files
- **Auditing**: all calls are logged in CloudTrail

## Practical example

**Scenario:** A Java application connects to an RDS PostgreSQL database using a username and password. Instead of placing credentials in `application.properties` (a huge risk if the repository is exposed), the team uses Secrets Manager: the password is stored in Secrets Manager, and the application retrieves credentials via SDK at runtime. Secrets Manager automatically rotates the password every 30 days, also updating RDS — the application always receives valid credentials without any human intervention.
