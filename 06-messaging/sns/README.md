# Amazon SNS (Simple Notification Service)

## What is it?

Amazon SNS is a fully managed pub/sub (publish/subscribe) messaging service that allows you to send notifications to multiple recipients simultaneously. A producer publishes a message to a **topic** and SNS delivers that message to all **subscribers** of that topic.

## Use cases

- Push notifications to mobile applications (iOS, Android)
- Sending alerts via email and SMS to operations teams
- Fan-out: trigger multiple parallel actions from a single event
- Real-time notifications for users
- Integration with SQS for fan-out architecture (SNS → multiple SQS queues)

## Key points for the exam (CLF-C02)

- **Pub/Sub model**: publishers send to topics; subscribers receive automatically
- **Delivery protocols**: HTTP/HTTPS, email, email-JSON, SMS, SQS, Lambda, mobile push applications
- **Fan-out pattern**: a message published to an SNS topic is delivered simultaneously to multiple SQS queues — classic pattern for parallel processing
- **Push-based**: SNS pushes messages to subscribers (unlike SQS, where the consumer pulls)
- **SNS FIFO**: topics with ordered delivery and no duplicates — for cases requiring ordering
- **Message Filtering**: subscribers can filter which messages they receive based on attributes — avoids processing irrelevant messages
- **No retention**: SNS does not store messages — if a subscriber is unavailable, the message is lost (use SQS to guarantee delivery)
- Limit of **12.5 million subscriptions** per topic

## Practical example

**Scenario:** An infrastructure monitoring system detects a server with CPU above 90%. A CloudWatch alarm publishes a message to the SNS topic `CriticalAlerts`. SNS simultaneously delivers: (1) an email to the Ops team, (2) an SMS to the on-call support, (3) a message to an SQS queue that triggers a Lambda to automatically try to remediate the issue. A single event triggers three parallel actions.
