# Amazon EBS (Elastic Block Store)

## What is it?

Amazon EBS is a high-performance block storage service designed for use with EC2 instances. It works like a virtual HDD/SSD that can be attached to an EC2 instance, providing persistent storage that survives instance shutdown.

## Use cases

- Operating system disk for EC2 instances
- Database storage (MySQL, PostgreSQL, Oracle)
- Applications requiring low latency and high I/O performance
- Transactional data storage that must persist
- Boot volumes for EC2 instances

## Key points for the exam (CLF-C02)

- **Bound to a single AZ** — an EBS volume can only be attached to an EC2 instance in the same Availability Zone
- **Persistent**: data survives instance shutdown (unlike Instance Store)
- **EBS volume types:**
  - **gp3/gp2** (General Purpose SSD): general use, balances price and performance — most common
  - **io2/io1** (Provisioned IOPS SSD): high performance for critical databases
  - **st1** (Throughput Optimized HDD): big data, data warehouses — high throughput
  - **sc1** (Cold HDD): rarely accessed data — cheapest
- **Snapshots**: incremental EBS backups stored in S3 — can be used to create volumes in other AZs/regions
- **Different from S3**: EBS is block storage (like a hard drive); S3 is object storage (like a file server)
- A volume can be **attached to only one EC2 instance** at a time (except io1/io2 with Multi-Attach)
- You pay for provisioned capacity, not actual usage

## Practical example

**Scenario:** A PostgreSQL database runs on an EC2 instance with a 500 GB `gp3` EBS volume as the data disk. The team configures automated daily snapshots via AWS Backup. When the instance needs more space, the volume is expanded from 500 GB to 1 TB without downtime — and when the database needs to migrate to another region, the snapshot is copied to the new region and a new volume is created from it.
