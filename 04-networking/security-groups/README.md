# Security Groups

## What is it?

Security Groups are virtual firewalls that control inbound and outbound traffic for AWS resources such as EC2 instances, RDS, and others. They operate at the resource (instance) level and are stateful — if an inbound request is allowed, the outbound response is automatically allowed.

## Use cases

- Control which IP addresses can access a web server (port 80/443)
- Restrict SSH access (port 22) to only the office's IP addresses
- Allow only the application server to communicate with the database (port 3306)
- Create rules based on other Security Groups (e.g., "accept traffic only from the Load Balancer")
- Isolate layers of a multi-tier application

## Key points for the exam (CLF-C02)

- **Stateful**: if inbound traffic is allowed, the return traffic is automatically allowed (no explicit outbound rule needed)
- **Allow rules only** — you cannot create DENY rules in Security Groups (use Network ACL for blocking)
- By default: **all inbound traffic is blocked** and **all outbound traffic is allowed**
- Can be attached to **multiple instances** — and one instance can have **multiple Security Groups**
- Rules can reference **other Security Groups** (not just IPs) — very powerful for layered architectures
- Operate at the **instance/resource level** — unlike Network ACL, which operates at the subnet level
- Rule changes are applied **immediately** to all associated instances
- **Security Group vs Network ACL**: SG = stateful, Allow only, instance level; NACL = stateless, Allow and Deny, subnet level

## Practical example

**Scenario:** A 3-tier web architecture defines: SG-Web (accepts HTTP/HTTPS from any IP, SSH only from the office IP); SG-App (accepts traffic on port 8080 only from SG-Web); SG-DB (accepts MySQL connections on port 3306 only from SG-App). This way, the database is completely unreachable from the internet, even if someone tries to access it directly — traffic only reaches the database if it comes from the application server.
