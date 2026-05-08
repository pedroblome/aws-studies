# AWS Elastic Beanstalk

## What is it?

AWS Elastic Beanstalk is a **PaaS (Platform as a Service)** that simplifies the deployment and management of web applications. You upload your code and Beanstalk automatically handles capacity provisioning, load balancing, scaling, and monitoring — without needing to manage the infrastructure directly.

## Use cases

- Rapid deployment of web applications for teams that do not want to manage infrastructure
- Agile development and staging environments
- Migrating on-premises applications to the cloud with minimal changes
- Startups focused on the product, not the infrastructure
- Applications in languages such as Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker

## Key points for the exam (CLF-C02)

- **PaaS**: you manage only the code and application configuration — AWS manages the rest
- Beanstalk itself is **free** — you pay only for the underlying resources it provisions (EC2, RDS, ELB, etc.)
- Supports multiple environments (production, staging) with isolated deployments
- Maintains **full control** over resources — unlike Lambda, you can still access the EC2 instances
- Automatically manages: EC2 provisioning, Load Balancer configuration, Auto Scaling, monitoring via CloudWatch
- Ideal for **quick deployments** without AWS infrastructure expertise
- **Not recommended** for highly customized architectures — in those cases, managing EC2/ECS directly is better

## Practical example

**Scenario:** A development agency needs to quickly deliver a Node.js application to a client. Using Elastic Beanstalk, the developer uploads the code via CLI (`eb deploy`). Beanstalk automatically creates EC2 instances, configures Nginx, enables Auto Scaling and the Load Balancer, and makes the application available at a public URL — all in less than 10 minutes, without the developer needing to know AWS infrastructure details.
