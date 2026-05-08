# Amazon EFS (Elastic File System)

## What is it?

Amazon EFS is a **shared and elastic** file system for use with AWS services and on-premises resources. Unlike EBS (which is attached to a single instance), EFS can be mounted simultaneously on multiple EC2 instances — it works like a network share (NFS).

## Use cases

- File sharing between multiple EC2 instances (content management systems)
- Shared storage for clustered web applications
- Big data and analytics processing that requires shared access
- Development environments with a shared filesystem across the team
- Containers (ECS/EKS) that need shared persistent storage

## Key points for the exam (CLF-C02)

- **Multi-AZ**: EFS is accessible across multiple Availability Zones in the same region — high availability by default
- **Automatic scalability**: grows and shrinks automatically as you add or remove files — no capacity provisioning needed
- **NFS protocol**: compatible with Linux/Unix (does not natively support Windows)
- **Performance modes**:
  - **General Purpose**: for most use cases (lower latency)
  - **Max I/O**: for highly parallel workloads (big data, media processing)
- **Storage classes**:
  - **EFS Standard**: frequently accessed data
  - **EFS Infrequent Access (IA)**: rarely accessed data — lower cost
- **More expensive than EBS and S3** — use only when you need shared storage across instances
- **EFS vs EBS**: EFS = shared (multi-instance, multi-AZ); EBS = exclusive (one instance, one AZ)

## Practical example

**Scenario:** A CMS (Content Management System) runs on 5 EC2 instances behind a Load Balancer. Images and media files uploaded by users must be available across all instances — if one instance receives the upload, the others need to access the same file. EFS is mounted on all 5 instances as `/var/www/uploads`, and any file saved by one instance is automatically available to all the others.
