# Amazon EventBridge

## What is it?

Amazon EventBridge is a serverless event bus that makes it easy to build event-driven applications. It connects different applications using events — receiving events from AWS sources, SaaS partners, or custom applications and routing them to targets such as Lambda, SQS, SNS, Step Functions, and more.

## Use cases

- Event-driven microservice orchestration
- Operations automation (e.g., automatic snapshots when an EC2 is started)
- Task scheduling (modern replacement of CloudWatch Events for cron jobs)
- Integration with SaaS applications (Datadog, Zendesk, Shopify) without intermediate code
- Routing and auditing security events (GuardDuty, Security Hub)

## Key points for the exam (CLF-C02)

- **Event Bus**: channel where events flow — there is a default bus (AWS events), partner buses, and custom buses
- **Rules**: filter events based on patterns and route them to targets — you define "if the event is X, send to Y"
- **Targets**: where the event is sent — Lambda, SQS, SNS, Step Functions, EC2, Kinesis, API Gateway, etc. (up to 5 targets per rule)
- **Schema Registry**: catalog of event schemas — facilitates development with autocomplete and validation
- **EventBridge Scheduler**: schedules tasks at specific times or intervals (e.g., run Lambda every day at 8am)
- **Difference from SNS**: EventBridge has content-based routing and integrates with 200+ SaaS sources; SNS is simpler and focused on notifications
- **Successor to CloudWatch Events**: CloudWatch Events was renamed to EventBridge — same functionality, more features
- **Serverless and managed**: no infrastructure to manage, scales automatically

## Practical example

**Scenario:** A company wants to automate security actions. When AWS GuardDuty detects suspicious activity, it publishes an event to EventBridge. A rule filters events with high severity and routes them simultaneously to: (1) a Lambda function that automatically blocks the suspicious IP in WAF, (2) an SQS queue that notifies the security team, (3) an S3 record for audit purposes. Everything is automated without human intervention.
