# IAM Policies

## What is it?

IAM Policies are JSON documents that define permissions — what is allowed or denied, on which resources, and under which conditions. They are attached to users, groups, or roles to control access to AWS services and resources.

## Use cases

- Define granular permissions (e.g., allow reads on S3 but deny deletions)
- Create reusable corporate policies applied to groups of developers
- Restrict access by condition (e.g., only from specific IPs, only when MFA is active)
- Apply maximum permission limits with **Permissions Boundaries**
- Control what member accounts can do via **Service Control Policies (SCPs)**

## Key points for the exam (CLF-C02)

- There are two main types:
  - **Managed Policies**: created and managed by AWS (AWS Managed) or by the customer (Customer Managed) — reusable
  - **Inline Policies**: embedded directly in a user, group, or role — 1:1 relationship
- Policy structure: **Effect** (Allow/Deny), **Action** (e.g., `s3:GetObject`), **Resource** (resource ARN)
- **Explicit Deny always overrides Allow** — permission evaluation hierarchy
- By default, everything is denied (**implicit deny**) — an explicit Allow is required
- Policies are evaluated at request time, not at creation time
- **SCP (Service Control Policy)** — used in AWS Organizations to restrict entire accounts

## Practical example

**Scenario:** The security team creates a Customer Managed Policy called `S3ReadOnlyProduction` that allows `s3:GetObject` and `s3:ListBucket` only on the `my-company-production` bucket. This policy is attached to the `Auditors` group. When a new auditor is added to the group, they immediately inherit the permissions — no individual reconfiguration needed.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::my-company-production",
        "arn:aws:s3:::my-company-production/*"
      ]
    }
  ]
}
```
