# AWS Shield

## What is it?

AWS Shield is a managed DDoS (Distributed Denial of Service) protection service. It protects applications running on AWS against attacks that attempt to make services unavailable through large volumes of malicious traffic.

## Use cases

- Protecting high-availability web applications against DDoS attacks
- Protecting critical infrastructure (banking, government, healthcare)
- Automatic protection of AWS resources without additional configuration
- Specialized 24/7 DDoS support (Shield Advanced)
- Compliance with requirements that mandate active DDoS protection

## Key points for the exam (CLF-C02)

- **Two levels of protection:**
  - **AWS Shield Standard**:
    - **Free** and automatically enabled for all AWS customers
    - Protection against DDoS attacks at Layers 3 and 4 (network and transport)
    - Mitigates volumetric attacks such as UDP floods and SYN floods
  - **AWS Shield Advanced**:
    - Paid (~$3,000/month per organization)
    - Additional protection against sophisticated Layer 7 (application) attacks
    - Access to the AWS **DRT (DDoS Response Team)** — specialized 24/7 support
    - **Cost protection**: reimbursement of scaling costs caused by a DDoS attack
    - Advanced diagnostics and attack reports
    - Protection for EC2, ELB, CloudFront, Route 53, AWS Global Accelerator
- **Shield vs WAF**: Shield = DDoS (volumetric, Layers 3/4); WAF = malicious HTTP request filtering (Layer 7)
- Shield Advanced can be integrated with WAF for combined protection

## Practical example

**Scenario:** A news portal goes offline during a major political event due to a volumetric DDoS attack. After the incident, the team migrates to Shield Advanced: a 100 Gbps attack is automatically mitigated before reaching the infrastructure. The security team receives real-time notifications about the attack and can engage the AWS DRT via chat if specialized support is needed. Extra EC2 costs caused by the attack are reimbursed by AWS — financial protection included.
