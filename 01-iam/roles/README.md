# IAM Roles

## What is it?

IAM Roles are AWS identities with specific permissions that can be temporarily assumed by users, applications, or AWS services. Unlike IAM users, roles do not have long-term credentials — credentials are generated dynamically and expire automatically.

## Use cases

- Allow EC2 instances to access S3 without storing access keys on the server
- Grant cross-account access between AWS accounts
- Allow AWS services (Lambda, ECS, etc.) to interact with other services
- Federated access — users authenticated via Active Directory or external identity providers (Google, Facebook) assume a role
- Temporary access for external auditors without creating permanent users

## Key points for the exam (CLF-C02)

- Roles provide **temporary, automatically rotated credentials** via AWS STS (Security Token Service)
- They are the **recommended** way to grant permissions to AWS services (e.g., Lambda, EC2)
- A role has a **Trust Policy** (who can assume the role) and a **Permission Policy** (what they can do)
- There is no username/password associated with a role — it is "assumed"
- Widely used in **identity federation** scenarios with corporate SSO
- Can be assigned to EC2 instances via an **Instance Profile**

## Practical example

**Scenario:** An application running on an EC2 instance needs to read objects from an S3 bucket. Instead of storing access keys on the instance (a security risk), the administrator creates an IAM Role with the `AmazonS3ReadOnlyAccess` policy and attaches it to the EC2's Instance Profile. The application automatically calls the instance metadata service to obtain temporary credentials — with no hardcoded keys in the code.
