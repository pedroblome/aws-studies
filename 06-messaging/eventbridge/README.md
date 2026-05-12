# Amazon EventBridge

## What is it?

Amazon EventBridge is a serverless event bus that makes it easy to build event-driven applications. It acts as the central nervous system of your architecture: services emit events, EventBridge evaluates rules against those events, and routes matching events to one or more targets — all without you writing any glue code.

It is the evolution of CloudWatch Events, with far more capabilities: integration with 200+ SaaS partners, content-based routing via event patterns, and its own schema registry.

## How it works

```
[Event Source]         →    [Event Bus]    →    [Rule: pattern match]    →    [Target(s)]
 AWS services                                                                   Lambda
 SaaS partners              default bus         { "source": "aws.ec2",         SQS
 Your own app               custom bus            "detail-type": [...] }        SNS
                            partner bus                                         Step Functions
                                                                                API Gateway
                                                                                Kinesis
```

1. An **event source** emits a JSON event
2. The event lands on an **event bus**
3. **Rules** evaluate each event against an event pattern (JSON filter)
4. Matching events are sent to up to **5 targets** per rule simultaneously

## Event Bus types

| Type | Purpose |
|---|---|
| **Default** | Receives all AWS service events automatically |
| **Custom** | For your own application events — you publish events with `PutEvents` |
| **Partner** | Receives events from SaaS partners (Datadog, Zendesk, Shopify, etc.) |

## Key concepts

- **Event Pattern**: a JSON filter that matches against the event's fields. Supports exact match, prefix, suffix, `anything-but`, `exists`, numeric ranges, and more. No code needed.
- **Rules**: bind an event pattern to one or more targets. You can also use a **Schedule** (cron or rate) instead of a pattern — replacing CloudWatch Events for scheduled tasks.
- **Targets**: where matched events are sent. Each rule supports up to 5 targets simultaneously, enabling fan-out from a single rule.
- **EventBridge Scheduler**: dedicated service for scheduling tasks (cron expressions or fixed-rate). More powerful than CloudWatch Events — can schedule millions of tasks with per-target timezone support.
- **Schema Registry**: automatically discovers the schema of events flowing through your bus and generates code bindings for Java, Python, TypeScript — makes development much faster.
- **Archive & Replay**: you can archive all events on a bus and replay them later — invaluable for debugging and re-processing after a bug fix.
- **Pipes**: point-to-point integration that enriches, filters, and routes events between a source and a target with minimal code.

## When to use EventBridge

Use EventBridge when you need:
- **React to AWS service events** (EC2 state change, S3 object created, CodePipeline failed, etc.)
- **Decouple microservices** with a central event router rather than point-to-point calls
- **Content-based routing** — different targets based on what's inside the event
- **SaaS integrations** without writing HTTP polling code
- **Scheduled automation** (cron jobs, nightly reports, cleanup tasks)
- **Audit trail** of all events via archive

**Do NOT use EventBridge when:** you need guaranteed delivery with retry under consumer failure (use SQS), high-throughput ordered streaming (use Kinesis), or pure notifications to many subscribers (use SNS).

## SQS vs SNS vs EventBridge vs Kinesis

| Feature | SQS | SNS | EventBridge | Kinesis |
|---|---|---|---|---|
| Model | Pull queue | Push pub-sub | Event bus + rules | Data stream |
| Routing | None (FIFO only) | Topic-based | Content-based patterns | Shard-based |
| Sources | Your app | Your app | AWS + SaaS + your app | Your app |
| Replay | No | No | Yes (archive) | Yes (7–365 days) |
| Targets per event | 1 consumer group | Many subscribers | Up to 5 per rule | Many consumers |
| Best for | Work queues | Fan-out notifications | Event-driven automation | Real-time analytics |

## Key points for the exam (CLF-C02 / SAA-C03)

- EventBridge is the **successor to CloudWatch Events** — same API, more features
- Default bus receives **all AWS service events** automatically (no configuration needed)
- Rules support **content-based routing** — filter on any field inside the event JSON
- Up to **5 targets per rule**, all invoked simultaneously (fan-out)
- **EventBridge Scheduler** replaces cron-based CloudWatch Events and supports millions of schedules
- **Archive and Replay** — can replay past events after a bug fix without re-running the original action
- Integrates with **200+ SaaS partners** via partner event buses (no polling code required)
- Schema Registry enables **auto-generated code** for your events

## Practical example

**Scenario — Automated infrastructure governance:**

Your company has a rule: any EC2 instance started without a "CostCenter" tag must be automatically stopped and the team notified.

1. AWS emits an `EC2 Instance State-change Notification` event to the default EventBridge bus every time an instance starts
2. A rule matches events where `detail.state = "running"`
3. The rule sends the event to **two targets simultaneously**:
   - A Lambda function that calls the EC2 API to check tags — if "CostCenter" is missing, stops the instance
   - An SQS queue that a notification service reads to send a Slack alert to the team

```
[EC2 starts]
     ↓
[EventBridge Default Bus]
     ↓  Rule: state=running
     ├──→ Lambda: check tags → stop untagged instance
     └──→ SQS → notification service → Slack alert
```

No polling. No scheduled scripts. The moment an instance starts, the rule fires in under a second.

**Scenario — Scheduled nightly cleanup:**

Use **EventBridge Scheduler** with a cron expression `cron(0 3 * * ? *)` (3 AM UTC daily) to trigger a Lambda function that deletes temporary DynamoDB records older than 24 hours — a modern, serverless replacement for cron jobs on EC2.
