# AWS Lambda

## What is it?

AWS Lambda is a **serverless** compute service that runs your code in response to events, without you needing to provision or manage servers. You pay only for the execution time of the code — measured in milliseconds.

## Use cases

- Serverless APIs and backends (integrated with API Gateway)
- Real-time event processing (S3 uploads, SQS/SNS messages)
- Task automation and scheduling (similar to cron, via EventBridge)
- Data transformation and processing (lightweight ETL)
- Webhooks and system integrations

## Key points for the exam (CLF-C02)

- **Serverless**: you do not manage servers — AWS handles all the infrastructure
- **Event-driven**: Lambda is triggered by events (HTTP via API Gateway, S3 upload, SQS message, etc.)
- **Pricing**: charged by number of requests and execution duration — the first 1 million requests/month are free (permanent free tier)
- **Maximum execution time**: 15 minutes per invocation
- **Supported languages**: Python, Node.js, Java, Go, Ruby, C#, and custom runtimes
- **Scales automatically**: from zero to thousands of concurrent executions without configuration
- **Lambda is FaaS** (Function as a Service) — the smallest abstraction level in the serverless model
- Integrates natively with dozens of AWS services

## Practical example

**Scenario:** An e-commerce platform needs to automatically resize images uploaded by users. When a user uploads a photo to an S3 bucket, an event triggers a Lambda function that processes the image (resizes, compresses), saves the optimized version to another S3 bucket, and logs the result in DynamoDB. All without servers — the team does not need to manage any infrastructure.
