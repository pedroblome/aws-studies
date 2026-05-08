# AWS CloudTrail

## What is it?

AWS CloudTrail is a service that records and monitors all API calls made in your AWS account — who did what, when, and from where. It provides a complete history of events for auditing, compliance, operational analysis, and security incident investigation.

## Use cases

- Security auditing — find out who deleted a resource or changed an IAM policy
- Regulatory compliance (PCI DSS, HIPAA, SOC 2) that requires audit logs
- Security incident investigation (who accessed what and when)
- Detect unauthorized changes to account configuration
- Operational analysis of API usage patterns

## Key points for the exam (CLF-C02)

- **Enabled by default** on all AWS accounts — records the last 90 days of management events for free
- **Event types:**
  - **Management Events**: control-plane operations on the account (create/delete resources, modify policies) — enabled by default
  - **Data Events**: data-plane operations (e.g., GetObject on S3, Lambda Invoke) — must be explicitly enabled (additional cost)
  - **Insights Events**: automatically detects unusual API activity
- **Trail**: configuration that sends events to an S3 bucket for long-term retention (beyond the default 90 days)
- **CloudTrail vs CloudWatch**:
  - CloudTrail = "who did what" — auditing and compliance
  - CloudWatch = "what is happening" — metrics and performance
- **Encryption**: logs are encrypted with SSE-S3 by default; KMS can be used for more control
- **Log integrity**: CloudTrail verifies that logs have not been altered after creation
- Logs contain: caller identity, time, service called, source IP address, parameters, and response

## Practical example

**Scenario:** A company discovers that an S3 bucket containing confidential data was accidentally made public. Using CloudTrail, the security team searches the logs for the `PutBucketPublicAccessBlock` event at the suspicious time. Within minutes, they identify that the IAM user `temp-developer` made the change at 11:47pm from an IP address in the city. The user is immediately deactivated and the change is reverted — and the incident triggers a new permissions review process.
