# AWS KMS (Key Management Service)

## What is it?

AWS KMS is a managed service that makes it easy to create and control the encryption keys used to protect your data. It integrates with dozens of AWS services to encrypt data at rest and in transit, and provides granular access control over who can use which keys.

## Use cases

- Encrypt data at rest in S3, EBS, RDS, DynamoDB, etc.
- Manage the lifecycle of cryptographic keys
- Digitally sign and verify documents
- Encrypt secrets and sensitive data in applications
- Meet compliance requirements that mandate managed encryption

## Key points for the exam (CLF-C02)

- **CMK (Customer Master Key)**: key managed by KMS — can be AWS Managed or Customer Managed
  - **AWS Managed Key**: created and managed by AWS, automatic annual rotation — you use it but don't control it
  - **Customer Managed Key (CMK)**: created and controlled by you — define access policies, rotation, and auditing
- **KMS does not store your keys on disk** — keys are kept in secure HSMs (Hardware Security Modules)
- **Key Policy**: policy that controls who can use and administer the key
- **Automatic rotation**: customer-managed CMKs can have annual automatic rotation enabled
- **Native integration** with S3, EBS, RDS, Lambda, SSM Parameter Store, Secrets Manager, and others
- **Envelope Encryption**: KMS generates a data key to encrypt the data; the CMK encrypts the data key — never the data directly
- **Auditable**: all KMS calls are logged in CloudTrail
- **Multi-Region Keys**: key replicas in multiple regions for global workloads

## Practical example

**Scenario:** A bank needs to encrypt customer data in S3. The team creates a CMK in KMS with a key policy that allows only the `AppProduction` role and the `SecurityIT` IAM group to use the key. When the application saves data to S3, S3 uses KMS to encrypt it automatically. If a developer without permission tries to download the file, S3 attempts to decrypt it with KMS — and the request is denied by the key policy. All attempts are recorded in CloudTrail.
