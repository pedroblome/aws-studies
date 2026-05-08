# High Availability

## What is it?

High Availability (HA) is the ability of a system to remain operational and accessible for a long period, even in the face of individual component failures. On AWS, HA is achieved by distributing resources across multiple Availability Zones (AZs) and regions, with automatic failover.

## Use cases

- Business-critical applications that cannot have downtime (banking, e-commerce, healthcare)
- Systems that require 99.99% SLA or higher
- Protection against datacenter failures and planned maintenance
- Automatic disaster recovery
- Production environments with millions of users

## Key points for the exam (CLF-C02)

**Fundamental concepts:**

- **High Availability vs Fault Tolerance:**
  - HA = the system remains operational after a failure (there may be a brief interruption)
  - Fault Tolerance = the system operates with NO interruption even during failures (more expensive and complex)

- **Region vs Availability Zone:**
  - Region: geographic area with multiple datacenters (e.g., us-east-1 = N. Virginia)
  - AZ (Availability Zone): isolated datacenter(s) within a region — connected by low-latency fiber

**HA patterns on AWS:**

1. **Multi-AZ**: distribute resources (EC2, RDS, ElastiCache) across 2+ AZs with automatic failover
2. **Auto Scaling**: automatically replace failed instances with new healthy ones
3. **Elastic Load Balancer**: distribute traffic across healthy instances in multiple AZs
4. **RDS Multi-AZ**: synchronous standby replica — automatic failover in under 2 minutes
5. **Route 53 Health Checks + Failover**: redirect traffic to a backup region if the primary fails

**Availability SLAs:**
- 99.9% = 8.7 hours of downtime/year
- 99.99% = 52 minutes of downtime/year
- 99.999% = 5 minutes of downtime/year (five nines)

## Practical example

**Scenario:** A bank designs its web application for 99.99% availability. The architecture uses: an ALB distributing traffic across EC2 instances in 2 AZs (us-east-1a and us-east-1b) with an Auto Scaling Group minimum of 2 instances; Aurora RDS with Multi-AZ and automatic failover; ElastiCache Redis in a multi-AZ cluster; Route 53 with health checks and failover to a secondary region (us-west-2). When AZ us-east-1a goes down for maintenance, traffic is automatically redirected to us-east-1b — without any user noticing.
