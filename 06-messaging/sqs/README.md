# Amazon SQS (Simple Queue Service)

## What is it?

Amazon SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It allows one component to send messages to the queue without requiring the recipient to be available at the time of sending.

## Use cases

- Decouple application components (independent producers and consumers)
- Process background tasks (sending emails, generating reports, processing images)
- Absorb traffic spikes — the queue acts as a buffer
- Ensure no messages are lost even if the consumer is offline
- Asynchronous communication between microservices

## Key points for the exam (CLF-C02)

- **Queue types:**
  - **Standard Queue**: high throughput, at-least-once delivery, no guaranteed order — for most use cases
  - **FIFO Queue**: exactly-once delivery, guaranteed order, lower throughput (300 msg/s) — for processes that require ordering
- **Retention Period**: messages stay in the queue from 1 minute to 14 days (default: 4 days)
- **Visibility Timeout**: after the consumer receives a message, it becomes invisible for a period — if not deleted, it returns to the queue
- **Dead Letter Queue (DLQ)**: separate queue for messages that have failed multiple times — facilitates debugging
- **Long Polling**: the consumer waits until a message is available (reduces empty calls and costs)
- **Maximum message size**: 256 KB (use S3 + SQS for larger messages)
- **SQS vs SNS**: SQS = pull (consumer fetches messages); SNS = push (messages sent to subscribers)

## Practical example

**Scenario:** An e-commerce platform processes orders at high speed. Instead of the web server processing payment synchronously (making the user wait), it sends the order to an SQS queue and immediately responds to the user. A set of Lambda workers consumes the queue and processes payments asynchronously. During Black Friday, the queue absorbs 100,000 orders without overwhelming the payment system — orders are processed at the pace the system can handle.
