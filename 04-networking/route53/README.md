# Amazon Route 53

## What is it?

Amazon Route 53 is AWS's managed, scalable DNS (Domain Name System) service. It translates human-readable domain names (such as `www.mycompany.com`) into IP addresses. In addition to DNS, it offers domain registration and endpoint health checks.

## Use cases

- Register domains and manage DNS for applications hosted on AWS
- Intelligent traffic routing based on latency, geolocation, or weight
- Automatic failover — redirect traffic to a backup endpoint if the primary fails
- Integration with other AWS services (ELB, CloudFront, S3 static websites)
- Private DNS for resources within a VPC

## Key points for the exam (CLF-C02)

- **Highly available and scalable** — designed with a 100% availability SLA
- **Routing policies:**
  - **Simple**: basic routing to a single resource
  - **Weighted**: distributes traffic between resources with weights (e.g., 70% to v1, 30% to v2 — useful for blue/green deploy)
  - **Latency-based**: directs users to the region with the lowest latency
  - **Failover**: redirects to backup if the primary fails (with health checks)
  - **Geolocation**: routes based on the user's geographic location
  - **Geoproximity**: routes based on geographic proximity (with configurable bias)
  - **Multivalue Answer**: returns multiple IPs and removes unhealthy ones
- **Health Checks**: monitor endpoint availability and trigger failover
- **Hosted Zones**: containers of DNS records for a specific domain (public or private)
- The name "Route 53" comes from port 53, the default port for the DNS protocol

## Practical example

**Scenario:** A global company has servers in regions us-east-1, eu-west-1, and ap-southeast-1. Route 53 uses latency-based routing: users from the Americas are directed to us-east-1, Europeans to eu-west-1, and Asians to ap-southeast-1 — each receives a response from the closest server. If the us-east-1 server fails, health checks detect the failure within seconds and Route 53 automatically redirects American traffic to eu-west-1.
