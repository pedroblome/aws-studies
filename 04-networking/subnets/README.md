# Subnets

## What is it?

Subnets are segments of a VPC that reside within a single Availability Zone (AZ). They divide the VPC's IP address space into smaller blocks and allow you to organize and isolate resources by function, access level (public/private), and security.

## Use cases

- Separate public resources (web servers) from private resources (databases)
- Isolate layers of an application (web tier, app tier, data tier)
- Distribute resources across multiple AZs for high availability
- Create dedicated networks for specific services (e.g., a subnet for RDS, another for EC2)

## Key points for the exam (CLF-C02)

- **Public subnet**: has a route to an Internet Gateway — resources can have public IPs and receive traffic from the internet
- **Private subnet**: no direct route to the internet — resources are only accessible from within the VPC or via VPN
- Each subnet belongs to **exactly one AZ** — use multiple subnets in different AZs for high availability
- **5 IP addresses are reserved** by AWS in each subnet (first, second, third, second-to-last, and last)
- **NAT Gateway**: placed in a public subnet to allow instances in private subnets to access the internet
- **Bastion Host (Jump Box)**: an EC2 instance in a public subnet used to SSH into instances in private subnets
- The subnet's Route Table determines where traffic is directed (Internet Gateway, NAT Gateway, etc.)

## Practical example

**Scenario:** A banking application is deployed with high availability across 2 AZs. Architecture: 2 public subnets (one per AZ) with web servers and the Load Balancer; 2 private subnets (one per AZ) with application servers; 2 database subnets (one per AZ) with RDS instances. If one AZ fails, the other continues serving traffic — ensuring availability even in the event of a datacenter failure.
