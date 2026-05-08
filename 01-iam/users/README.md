# IAM Users

## What is it?

IAM Users are identities created inside your AWS account that represent a person or application interacting with AWS services. Each user has unique credentials (password and/or access keys) and specific permissions that control what they can do.

## Use cases

- Provide individual access to the AWS Management Console for team members
- Create programmatic credentials (Access Key ID + Secret Access Key) for applications and scripts
- Configure MFA (Multi-Factor Authentication) access for stronger security
- Audit individual activity per collaborator through AWS CloudTrail

## Key points for the exam (CLF-C02)

- An IAM user is an identity with long-term permissions — unlike roles, which provide temporary access
- By default, a new IAM user has no permissions at all (principle of least privilege)
- Users can belong to **IAM groups**, inheriting the group's policies
- **Root account** credentials should NOT be used for daily tasks — create IAM users with appropriate permissions
- MFA adds a second layer of security beyond the password
- Limit of **5,000 IAM users** per AWS account
- Access Keys are used for CLI/API access, not for the Console

## Practical example

**Scenario:** A company hired a new developer. The administrator creates an IAM user called `john.doe`, adds them to the `Developers` group (which already has EC2 and S3 access policies), and enables MFA. The developer uses their password to access the Console and their access keys to deploy via CLI — without ever needing the root credentials.
