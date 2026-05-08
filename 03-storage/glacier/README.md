# Amazon S3 Glacier

## What is it?

Amazon S3 Glacier is a **low-cost** cloud storage service designed for **data archiving** and **long-term backup**. Data stored in Glacier is rarely accessed but needs to be retained for months, years, or decades — typically for regulatory compliance purposes.

## Use cases

- Archiving medical records (legal retention obligation for 20+ years)
- Long-term backup of corporate data
- Archiving audit logs and compliance data
- Preservation of scientific and historical data
- Replacing physical magnetic tape (tape backup) systems

## Key points for the exam (CLF-C02)

- **Glacier variants** (within S3):
  - **S3 Glacier Instant Retrieval**: retrieval in milliseconds — ideal for data accessed quarterly
  - **S3 Glacier Flexible Retrieval**: retrieval in minutes (Expedited), hours (Standard), or 5–12 hours (Bulk) — cheaper
  - **S3 Glacier Deep Archive**: cheapest of all — retrieval within 12 hours (Standard) or 48 hours (Bulk)
- **Very low cost**: Deep Archive costs approximately $0.00099/GB/month — up to 23x cheaper than S3 Standard
- **Vault**: container for storing archives in Glacier (equivalent to an S3 bucket)
- **Archive**: each item stored in Glacier (equivalent to an S3 object)
- **Vault Lock**: immutable compliance policy — data cannot be deleted before a set deadline (WORM: Write Once Read Many)
- **S3 Lifecycle Policies** can automatically move data from S3 to Glacier after a defined period
- Not suitable for data that requires frequent or immediate access

## Practical example

**Scenario:** A hospital is legally required to retain medical records for 20 years. Records from the last 2 years remain in S3 Standard (frequent access for consultations). After 2 years, a Lifecycle Policy automatically moves them to S3 Standard-IA. After 5 years, data moves to S3 Glacier Deep Archive — costing cents per GB. A Vault Lock ensures data cannot be deleted before the legal deadline, satisfying regulatory compliance requirements.
