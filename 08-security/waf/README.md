# AWS WAF (Web Application Firewall)

## What is it?

AWS WAF is a web application firewall that protects your web applications and APIs against common internet exploits that could affect availability, compromise security, or consume excessive resources. It allows you to create rules that control HTTP/HTTPS traffic based on conditions you define.

## Use cases

- Protection against SQL Injection and Cross-Site Scripting (XSS) attacks
- Blocking malicious IPs and automated bots
- Protection against scrapers and API abuse
- Compliance with web application security requirements
- Traffic filtering by geolocation (block specific countries)

## Key points for the exam (CLF-C02)

- **Where WAF is deployed**: integrates with CloudFront, Application Load Balancer (ALB), API Gateway, AppSync
- **Web ACL (Access Control List)**: set of rules that WAF applies to traffic
- **Rules**: define blocking or allowing conditions — can inspect IP, HTTP headers, URI, request body, etc.
- **AWS Managed Rules**: pre-configured rule sets maintained by AWS for protection against OWASP Top 10, bots, etc.
- **Rate-based rules**: block IPs that exceed a number of requests in a period — protection against brute force
- **WAF vs Shield:**
  - WAF = Layer 7 protection (application) — filters malicious HTTP requests
  - Shield = Layer 3/4 protection (network/transport) — protection against volumetric DDoS
- **WAF logs**: can be sent to S3, CloudWatch Logs, or Kinesis Data Firehose for analysis
- **Pricing**: per Web ACL, per rule, and per million inspected requests

## Practical example

**Scenario:** A banking portal is experiencing SQL Injection attempts. The team configures WAF on CloudFront with: (1) AWS Managed Rule Group for OWASP Top 10 (automatically blocks SQL Injection, XSS); (2) a rate-limiting rule that blocks IPs with more than 100 requests per minute (brute force protection); (3) Geo-restriction blocking countries from which no legitimate customers originate. WAF inspects 100% of requests before they reach the application.
