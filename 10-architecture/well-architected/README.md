# AWS Well-Architected Framework

## What is it?

The AWS Well-Architected Framework is a set of best practices and design principles created by AWS to help cloud architects build secure, high-performance, resilient, and efficient infrastructure. It is based on six fundamental pillars that guide architectural decisions.

## Use cases

- Evaluating existing architectures to identify risks and improvement opportunities
- Guide for architecting new cloud applications from the start
- Periodic infrastructure review (Well-Architected Review)
- Preparation for compliance and security audits
- Alignment with industry best practices

## Key points for the exam (CLF-C02)

**The 6 Pillars of the Well-Architected Framework:**

1. **Operational Excellence**
   - Run and monitor systems, continuously improve processes and procedures
   - Principles: infrastructure as code, small and frequent changes, anticipate failures

2. **Security**
   - Protect data, systems, and assets
   - Principles: strong identity, traceability, security at all layers, encryption, incident preparedness

3. **Reliability**
   - Ability to recover from failures and meet demand
   - Principles: automatic recovery, test recovery procedures, scale horizontally, stop guessing capacity

4. **Performance Efficiency**
   - Use computing resources efficiently
   - Principles: democratize advanced technologies, go global in minutes, serverless architectures, experiment frequently

5. **Cost Optimization**
   - Avoid unnecessary spending
   - Principles: consumption-based model, measure efficiency, stop spending on data centers, analyze and attribute expenditures

6. **Sustainability** *(added in 2021)*
   - Minimize environmental impact
   - Principles: understand your impact, maximize utilization, use managed services, reduce downstream resources

## Practical example

**Scenario:** A company conducts a Well-Architected Review on its e-commerce application and identifies risks: (1) Security — RDS database in a public subnet (high risk); (2) Reliability — no Multi-AZ or automatic backups; (3) Cost Optimization — over-provisioned EC2 instances running at 5% CPU usage. The action plan moves RDS to a private subnet, enables Multi-AZ, activates automatic backups, and downsizes the instances — improving the architecture across all pillars.
