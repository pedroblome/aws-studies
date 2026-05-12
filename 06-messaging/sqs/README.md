# Amazon SQS (Simple Queue Service)

## What is it?

Amazon SQS is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. It allows one component to send messages to the queue without requiring the recipient to be available at the time of sending.

The producer puts a message in the queue; the consumer pulls that message when ready. SQS guarantees the message will not be lost and that at least one consumer will process it.

## How it works

```
[Producer]  →  puts message  →  [SQS Queue]  →  consumer polls  →  [Consumer / Lambda]
                                                                           ↓
                                                               deletes message after processing
```

The consumer must **explicitly delete** the message after successful processing. If not deleted within the Visibility Timeout window, the message becomes visible again and can be re-processed by another consumer.

## Queue types

| Feature | Standard Queue | FIFO Queue |
|---|---|---|
| Throughput | Unlimited (nearly) | 300 msg/s (3,000 with batching) |
| Order | Best-effort | Strict (First-In-First-Out) |
| Delivery | At-least-once (may duplicate) | Exactly-once |
| Use case | High-throughput, order doesn't matter | Order-critical, no duplicates allowed |
| Naming | Any name | Must end in `.fifo` |

## Key concepts

- **Visibility Timeout**: after a consumer receives a message, it becomes invisible for a configurable period (default 30s, max 12h). If not deleted, it returns to the queue — protects against consumer failures.
- **Dead Letter Queue (DLQ)**: a separate queue that receives messages that have failed processing a configured number of times (`maxReceiveCount`). Used for debugging and alerting on poison-pill messages.
- **Long Polling**: instead of constantly polling (which wastes money on empty responses), the consumer waits up to 20 seconds for a message to arrive — reduces cost and empty calls significantly.
- **Retention Period**: messages stay in the queue from 1 minute to 14 days (default: 4 days).
- **Maximum message size**: 256 KB — for larger payloads, store the data in S3 and put only the S3 reference in the SQS message (Extended Client Library pattern).
- **Delay Queues**: postpone delivery of new messages by 0–900 seconds.

## When to use SQS

Use SQS when you need:
- **Point-to-point** async communication (one producer, one consumer group)
- To **buffer and absorb traffic spikes** — the queue acts as a shock absorber
- **Guaranteed processing** even if the consumer is temporarily offline
- **Decoupling** two systems so they can scale independently
- Workers that **pull** work at their own pace (rate limiting, backpressure)

**Do NOT use SQS when:** you need to fan-out the same message to multiple independent consumers simultaneously (use SNS → SQS fan-out pattern instead), or when you need real-time streaming and replay of millions of events per second (use Kinesis).

## SQS vs SNS vs EventBridge vs Kinesis

| Service | Model | Best for |
|---|---|---|
| SQS | Pull / Queue | Point-to-point async work queues |
| SNS | Push / Pub-Sub | Fan-out notifications to multiple endpoints |
| EventBridge | Event Bus / Rules | Event routing, SaaS integration, automation |
| Kinesis | Streaming | Real-time high-volume data streams |

## Key points for the exam (CLF-C02 / SAA-C03)

- SQS = **pull-based** (consumer fetches); SNS = **push-based**
- **Standard** = max throughput, at-least-once; **FIFO** = ordered, exactly-once, lower throughput
- **Visibility Timeout** prevents two consumers from processing the same message simultaneously
- **DLQ** is a standard SQS queue — you configure it by setting the redrive policy on the source queue
- **Long Polling** (`WaitTimeSeconds > 0`) reduces cost vs. short polling
- Lambda can be an **event source** for SQS — Lambda polls the queue and invokes your function in batches

## Practical example

**Scenario — E-commerce order processing:**

A checkout service receives 50,000 orders during a Black Friday flash sale. Instead of processing payments synchronously (making users wait and potentially crashing the payment system), the checkout service puts each order into an SQS Standard Queue and immediately returns a confirmation to the user.

A fleet of Lambda functions polls the queue, processes one batch of 10 orders at a time, charges the credit card, updates inventory, and sends a confirmation email. If the payment processor is slow, orders queue up safely. If a Lambda times out mid-processing, the order reappears in the queue (Visibility Timeout expired) and is retried. After 3 failures, the order goes to a DLQ where the ops team is alerted via CloudWatch Alarm.

```
[Checkout API] → SQS Standard Queue → Lambda (batch size 10) → Payment Processor
                         ↓ (after maxReceiveCount failures)
                    Dead Letter Queue → CloudWatch Alarm → SNS → Ops Team Email
```
