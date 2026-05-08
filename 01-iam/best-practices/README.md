# IAM Best Practices

## What is it?

IAM best practices are a set of AWS recommendations for configuring and managing identities and access securely. Following these practices dramatically reduces the risk of security breaches and unauthorized access.

## Use cases

- Protect the AWS account from unauthorized access
- Meet compliance requirements (ISO 27001, SOC 2, PCI DSS)
- Implement the **Zero Trust** security model
- Periodically audit and review permissions and access

## Key points for the exam (CLF-C02)

1. **Do not use the root account** for daily tasks — protect it with MFA and store credentials in a safe place
2. **Create individual IAM users** — never share credentials between people
3. **Use groups to assign permissions** — it is easier to manage permissions in groups than individually
4. **Principle of Least Privilege** — grant only the minimum permissions necessary for the task
5. **Enable MFA** — especially for the root account and users with elevated privileges
6. **Use roles for applications** instead of hardcoded access keys in code
7. **Rotate credentials regularly** — access keys should be rotated periodically
8. **Use IAM Access Analyzer** to identify externally exposed resources
9. **Remove unused credentials** — unused users and keys are security risks
10. **Use AWS Organizations + SCPs** for centralized control in multi-account environments

## Practical example

**Scenario:** A startup begins with the owner using the root account for everything. After a security audit, the team adopts best practices: creates an IAM admin user for daily operations, enables MFA on the root and admin accounts, organizes developers into groups (`Developers`, `QA`, `Ops`) with specific policies for each, and configures IAM Access Analyzer to receive alerts if any S3 bucket is accidentally made public. Access keys are rotated every 90 days through internal policy.
