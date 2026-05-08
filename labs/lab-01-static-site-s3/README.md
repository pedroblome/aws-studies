# Lab 01 — Static Website with Amazon S3

## What is it?

In this lab, you will learn how to host a static website (HTML, CSS, JavaScript) using Amazon S3, configure public access, enable the static website hosting feature, and distribute the content globally with Amazon CloudFront. This is one of the simplest and most cost-effective use cases for hosting websites on AWS.

## Use cases

- Personal portfolios and presentation websites
- Project documentation (like this repository)
- Landing pages and institutional websites
- Frontend applications (React, Vue, Angular) with separate APIs
- High-traffic sites at low cost (S3 is much cheaper than a server)

## Key points for the exam (CLF-C02)

- S3 can natively host static websites — no server required
- The site is accessible via S3 URL: `http://bucket-name.s3-website-region.amazonaws.com`
- To use a custom domain (e.g., `www.mysite.com`), combine with **Route 53** and **CloudFront**
- **CloudFront** adds HTTPS (required for custom domains) and global caching
- **ACM (AWS Certificate Manager)**: free SSL/TLS certificate for use with CloudFront
- The bucket must have **Block Public Access disabled** and a **Bucket Policy** that allows public access (`s3:GetObject`)
- Static files = HTML, CSS, JS, images — no server-side processing
- **Very low cost**: pay only for storage (GB) and data transfer

## Practical example

**Conceptual scenario — Step by Step:**

1. **Create the S3 bucket**: name matching the domain (e.g., `www.mysite.com`) in the desired region
2. **Upload files**: `index.html`, `style.css`, images, and other assets
3. **Enable Static Website Hosting**: set `index.html` as the default document and `error.html` as the error page
4. **Configure public access**: disable Block Public Access and create a Bucket Policy allowing `s3:GetObject` for `*`
5. **Create a CloudFront distribution**: pointing to the S3 endpoint, enabling HTTPS with an ACM certificate
6. **Configure Route 53**: create a CNAME or Alias record pointing `www.mysite.com` to the CloudFront distribution

**Result**: site accessible globally via HTTPS at `https://www.mysite.com`, with content cached at CloudFront edge locations in over 400 locations around the world — with millisecond latency for users in any country.

**Estimated cost**: for a simple site with 10 GB of data and 100,000 visits/month, the total cost (S3 + CloudFront) is under $5/month.
