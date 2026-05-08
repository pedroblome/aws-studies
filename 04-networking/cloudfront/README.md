# Amazon CloudFront

## What is it?

Amazon CloudFront is AWS's Content Delivery Network (CDN). It distributes content (web pages, images, videos, APIs) globally through a network of **edge locations** (points of presence) around the world, delivering content with very low latency to end users.

## Use cases

- Accelerate the delivery of static and dynamic websites globally
- Media content distribution (video streaming)
- Protecting APIs with low global latency
- Secure distribution of software and updates
- DDoS protection integrated with AWS Shield
- Serve S3 content globally with low latency

## Key points for the exam (CLF-C02)

- **Edge Locations**: AWS points of presence where content is cached — there are many more edge locations than regions and AZs
- **Origin**: the original source of the content — can be an S3 bucket, an ELB, an EC2 instance, or any HTTP server
- **Cache**: CloudFront caches content at edge locations, reducing origin load and user latency
- **TTL (Time to Live)**: defines how long content is cached before being refreshed
- **HTTPS by default**: supports SSL/TLS with certificates managed by ACM (AWS Certificate Manager) for free
- **AWS Shield Standard**: DDoS protection **included for free** with CloudFront
- **Geo-restriction**: allows blocking or allowing access from specific countries
- **CloudFront vs direct S3**: CloudFront adds global caching and reduces latency; use CloudFront for globally accessed content

## Practical example

**Scenario:** A news portal is growing and receiving visits from all over the world. Static files (images, CSS, JS) are stored in an S3 bucket in the sa-east-1 (Sao Paulo) region. Without CloudFront, users in Europe or Asia experience high latency. With CloudFront configured, images are automatically cached at the edge locations closest to each user — a reader in Tokyo receives content from the edge location in Japan, reducing latency from ~300ms to ~5ms.
