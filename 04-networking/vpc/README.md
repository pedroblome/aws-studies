# Amazon VPC (Virtual Private Cloud)

## What is it?

Amazon VPC is a logically isolated private virtual network within the AWS Cloud. It is your own section of the AWS Cloud where you can launch AWS resources in a virtual network that you define and control — with full control over the network environment, including IP range selection, subnet creation, and configuration of route tables and gateways.

## Use cases

- Isolate production resources in a secure private network
- Create multi-tier environments (web, application, database) with separate networks
- Connect on-premises corporate network to AWS via VPN or Direct Connect
- Segment environments (dev, staging, production) into separate VPCs
- Meet compliance requirements that mandate network isolation

## Key points for the exam (CLF-C02)

- Every AWS account has a **default VPC** in each region — ready for immediate use
- A VPC spans an **entire region** — subnets are created within Availability Zones
- **CIDR Block**: defines the IP address range of the VPC (e.g., `10.0.0.0/16`)
- **Main components:**
  - **Subnets**: segments of the VPC within an AZ — can be public or private
  - **Internet Gateway (IGW)**: enables communication between the VPC and the internet
  - **Route Tables**: define where traffic is directed
  - **NAT Gateway**: allows instances in private subnets to access the internet (without being accessible from outside)
  - **Security Groups**: virtual firewall at the instance level (stateful)
  - **Network ACLs**: firewall at the subnet level (stateless)
- **VPC Peering**: connects two VPCs for private communication (even across accounts and regions)
- **VPC Endpoints**: private access to AWS services without going through the public internet

## Practical example

**Scenario:** A 3-tier application (web, app, database) is architected in a VPC with CIDR `10.0.0.0/16`. The web tier sits in public subnets (with Internet Gateway), the application tier in private subnets, and the database in isolated private subnets. Instances in private subnets use a NAT Gateway to download updates from the internet without being exposed. Security Groups restrict access: the database only accepts connections from the application tier.
