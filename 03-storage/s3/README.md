# Amazon S3 (Simple Storage Service)

## What is it?

Amazon S3 is a highly durable, scalable, and available object storage service. It lets you store and retrieve any amount of data from anywhere on the internet. Data is organized in **buckets** (containers) and each file is stored as an **object** with a unique key.

## Use cases

- Hosting static websites (HTML, CSS, JS)
- Storing and distributing media files (images, videos)
- Data backup and recovery
- Data lake for analytics and big data
- Application log storage
- Content distribution via CloudFront

## Key points for the exam (CLF-C02)

- **Durability**: 99.999999999% (11 nines) — data replicated across multiple datacenters
- **Storage classes** (cost vs. access frequency):
  - **S3 Standard**: frequently accessed data
  - **S3 Standard-IA** (Infrequent Access): infrequently accessed data that still requires rapid access
  - **S3 One Zone-IA**: cheaper, but stored in only one AZ
  - **S3 Glacier Instant Retrieval**: archival with millisecond access
  - **S3 Glacier Flexible Retrieval**: archival with minutes-to-hours access
  - **S3 Glacier Deep Archive**: cheapest, access within 12 hours — for rarely accessed data
  - **S3 Intelligent-Tiering**: automatically moves data between classes based on access patterns
- **Maximum object size**: 5 TB (multipart upload for files > 100 MB)
- S3 is a **global** service but buckets are created in a specific region
- **Bucket names are globally unique** across all of AWS
- **S3 Object Lock** and **Versioning** for data protection and compliance
- By default, all buckets and objects are **private**

## Practical example

**Scenario:** A streaming company stores videos in S3 Standard for recently released content (frequent access), moves them to S3 Standard-IA after 30 days, and to S3 Glacier Deep Archive after 1 year. S3 Lifecycle Policies automate these transitions, reducing storage costs by up to 80% over time. CloudFront distributes the content globally with low latency.
