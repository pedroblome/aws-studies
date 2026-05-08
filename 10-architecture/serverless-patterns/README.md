# Serverless Architecture Patterns

## What is it?

Serverless architecture is a cloud computing model where the provider manages all server infrastructure — the developer focuses only on the code. In AWS, serverless does not mean "no servers," but rather that you do not manage servers. Serverless patterns are combinations of AWS services that solve common problems without infrastructure provisioning.

## Use cases

- REST APIs and backends for mobile and web applications
- Real-time event processing (uploads, messages, streams)
- Workflow automation and orchestration
- Chatbots and virtual assistants
- Batch data processing without servers
- Webhooks and system integrations

## Key points for the exam (CLF-C02)

**Primary serverless services on AWS:**
- **Compute**: AWS Lambda
- **API**: Amazon API Gateway
- **Database**: Amazon DynamoDB, Aurora Serverless
- **Storage**: Amazon S3
- **Messaging**: Amazon SQS, SNS, EventBridge
- **Orchestration**: AWS Step Functions
- **Authentication**: Amazon Cognito

**Common architectural patterns:**

1. **Serverless API**: API Gateway → Lambda → DynamoDB
2. **Event Processing**: S3 Upload → Lambda → processing → S3/DynamoDB
3. **Fan-out**: SNS → multiple SQS queues → multiple Lambda functions (parallel processing)
4. **Workflow**: Step Functions orchestrates multiple Lambda functions in sequence with business logic
5. **Scheduled Jobs**: EventBridge Scheduler → Lambda (serverless cron replacement)

**Advantages of serverless:**
- **No server management**: complete focus on business code
- **Automatic scaling**: from zero to millions of requests with no configuration
- **Pay-per-use**: pay only for what you use — zero cost when there is no traffic
- **High availability**: built-in by default in managed services

## Practical example

**Scenario:** A delivery app needs to process orders in real time. Serverless architecture: the mobile app calls a REST API (API Gateway) → Lambda validates the order and saves it to DynamoDB → DynamoDB Streams triggers another Lambda → which publishes to SNS → which fans out to: (1) Lambda notifies the restaurant via SMS; (2) SQS queues the message for the tracking system. Step Functions orchestrates the order state machine (received → preparing → out for delivery → delivered). Zero servers — scales to 100,000 simultaneous orders automatically.
