# Lab 04 — Event-Driven Order Pipeline: SQS + EventBridge + Kinesis + Lambda

## What you will build

A fully serverless, event-driven order processing pipeline for an e-commerce platform. This lab connects **SQS**, **EventBridge**, and **Kinesis** together with **Lambda** functions so you can see exactly what each service does and why you would choose one over another.

```
                        ┌─────────────────────────────────────────────────┐
                        │               EVENT-DRIVEN PIPELINE              │
                        └─────────────────────────────────────────────────┘

[POST /order]
      │
      ▼
[Lambda: order-producer]
      │
      ├──→ SQS: orders-queue ──────────────────→ [Lambda: order-processor]
      │         (order processing job)                     │
      │                                          ┌─────────┴──────────┐
      │                                          │  process payment   │
      │                                          │  update inventory  │
      │                                          └─────────┬──────────┘
      │                                                    │
      │                                         [EventBridge: custom bus]
      │                                                    │
      │                               ┌────────────────────┼────────────────────┐
      │                               ▼                    ▼                    ▼
      │                    Rule: order.completed   Rule: order.failed    Rule: ALL events
      │                               │                    │                    │
      │                               ▼                    ▼                    ▼
      │                    [Lambda: notification]  [Lambda: retry-alert]  [Kinesis Stream]
      │                    (send confirm email)    (alert ops team)             │
      │                                                                         ▼
      └──→ Kinesis: clickstream ──────────────────────────────────→  [Lambda: analytics]
           (every user action)                                       (real-time metrics)
                                                                             │
                                                                             ▼
                                                                    [DynamoDB: metrics-table]
```

## Architecture explained

Each service has a distinct role:

| Service | Role in this pipeline | Why this service? |
|---|---|---|
| **SQS** | Holds order processing jobs | Decouples checkout from payment; absorbs spikes; retries on failure |
| **EventBridge** | Routes order outcome events | Content-based routing (completed vs failed); fan-out to multiple targets |
| **Kinesis** | Streams all user clickstream events | High-volume continuous stream; multiple consumers; replay capability |
| **Lambda** | All business logic | Serverless; triggered by each of the above; pay per use |

## What you will learn

- SQS Visibility Timeout and Dead Letter Queue in action
- EventBridge event patterns and content-based routing
- Kinesis shards, partition keys, and Lambda as a stream consumer
- Why you choose SQS (task queue) vs Kinesis (data stream) vs EventBridge (event router)
- How to compose these three services into a real architecture

---

## Prerequisites

- AWS account with admin access (or permissions for Lambda, SQS, EventBridge, Kinesis, DynamoDB, IAM)
- AWS CLI configured (`aws configure`)
- Python 3.12+
- Basic understanding of JSON

---

## Step 1 — Create the SQS Queue (Order Jobs)

This queue holds order processing jobs. If an order fails processing 3 times, it moves to the Dead Letter Queue for manual inspection.

### 1a. Create the Dead Letter Queue first

```bash
aws sqs create-queue \
  --queue-name orders-dlq \
  --attributes '{
    "MessageRetentionPeriod": "1209600"
  }'
```

Save the DLQ ARN from the output — you will need it in the next step.

```bash
# Get the DLQ ARN
aws sqs get-queue-attributes \
  --queue-url <DLQ_URL_FROM_ABOVE> \
  --attribute-names QueueArn
```

### 1b. Create the main orders queue with DLQ configured

```bash
aws sqs create-queue \
  --queue-name orders-queue \
  --attributes '{
    "VisibilityTimeout": "60",
    "MessageRetentionPeriod": "345600",
    "ReceiveMessageWaitTimeSeconds": "20",
    "RedrivePolicy": "{\"deadLetterTargetArn\":\"<DLQ_ARN>\",\"maxReceiveCount\":\"3\"}"
  }'
```

**Understanding the settings:**
- `VisibilityTimeout: 60` — After Lambda receives a message, it has 60 seconds to process and delete it. If Lambda times out or crashes, the message becomes visible again for retry.
- `ReceiveMessageWaitTimeSeconds: 20` — Long polling: Lambda waits up to 20 seconds for a message instead of returning empty immediately (saves money).
- `maxReceiveCount: 3` — After 3 failed processing attempts, the message goes to the DLQ.

---

## Step 2 — Create the Kinesis Stream (Clickstream)

This stream captures every user action on the platform (page views, clicks, add-to-cart, purchases).

```bash
aws kinesis create-stream \
  --stream-name clickstream \
  --shard-count 2
```

Wait for the stream to become ACTIVE:

```bash
aws kinesis describe-stream-summary --stream-name clickstream
# Wait until StreamStatus = ACTIVE
```

**Understanding the design:**
- **2 shards** = 2 MB/s read, 2,000 records/s write capacity
- We will use `user_id` as the partition key — events from the same user always go to the same shard, giving us per-user ordering
- Kinesis retains data for **24 hours by default** — if our analytics Lambda has a bug, we can replay

---

## Step 3 — Create the EventBridge Custom Bus

EventBridge's default bus receives AWS service events. For our application events, we create a custom bus.

```bash
aws events create-event-bus --name orders-bus
```

Save the ARN from the output.

---

## Step 4 — Create the DynamoDB Table (Metrics)

Our analytics Lambda will write real-time metrics here.

```bash
aws dynamodb create-table \
  --table-name clickstream-metrics \
  --attribute-definitions \
    AttributeName=metric_key,AttributeType=S \
    AttributeName=timestamp,AttributeType=S \
  --key-schema \
    AttributeName=metric_key,KeyType=HASH \
    AttributeName=timestamp,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST
```

---

## Step 5 — Create the IAM Role for Lambda

All Lambda functions will share a single execution role with the required permissions.

```bash
# Create the trust policy file
cat > /tmp/lambda-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "lambda.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# Create the role
aws iam create-role \
  --role-name lab04-lambda-role \
  --assume-role-policy-document file:///tmp/lambda-trust-policy.json

# Attach permissions
aws iam attach-role-policy \
  --role-name lab04-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam attach-role-policy \
  --role-name lab04-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess

aws iam attach-role-policy \
  --role-name lab04-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonKinesisFullAccess

aws iam attach-role-policy \
  --role-name lab04-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonEventBridgeFullAccess

aws iam attach-role-policy \
  --role-name lab04-lambda-role \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess

# Get the role ARN (save this for later)
aws iam get-role --role-name lab04-lambda-role --query 'Role.Arn' --output text
```

> Note: In production you would use least-privilege policies. For this lab, broad policies are fine.

---

## Step 6 — Deploy the Lambda Functions

### Lambda 1: order-producer

This function receives an HTTP-like event, puts the order into SQS, and sends a clickstream event to Kinesis.

**File: `lambda/order_producer.py`**

```python
import json
import boto3
import uuid
import time

sqs = boto3.client('sqs', region_name='us-east-1')
kinesis = boto3.client('kinesis', region_name='us-east-1')

QUEUE_URL = '<YOUR_ORDERS_QUEUE_URL>'
STREAM_NAME = 'clickstream'

def lambda_handler(event, context):
    order_id = str(uuid.uuid4())
    user_id = event.get('user_id', 'user-001')
    
    # 1. Send order job to SQS for reliable async processing
    order_payload = {
        'order_id': order_id,
        'user_id': user_id,
        'items': event.get('items', []),
        'total': event.get('total', 0),
        'created_at': int(time.time())
    }
    
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order_payload),
        MessageAttributes={
            'order_type': {
                'DataType': 'String',
                'StringValue': event.get('order_type', 'standard')
            }
        }
    )
    
    # 2. Send clickstream event to Kinesis for real-time analytics
    # partition_key = user_id ensures all events from the same user
    # go to the same shard (ordered per user)
    kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps({
            'event_type': 'order_placed',
            'user_id': user_id,
            'order_id': order_id,
            'total': event.get('total', 0),
            'timestamp': int(time.time())
        }),
        PartitionKey=user_id
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Order received',
            'order_id': order_id
        })
    }
```

**Deploy:**

```bash
cd lambda
zip order_producer.zip order_producer.py

aws lambda create-function \
  --function-name order-producer \
  --runtime python3.12 \
  --role <ROLE_ARN> \
  --handler order_producer.lambda_handler \
  --zip-file fileb://order_producer.zip \
  --timeout 30 \
  --environment Variables="{QUEUE_URL=<YOUR_QUEUE_URL>}"
```

---

### Lambda 2: order-processor (SQS Consumer)

This function is triggered by SQS. It processes the payment and publishes the outcome to EventBridge.

**File: `lambda/order_processor.py`**

```python
import json
import boto3
import random
import time

events_client = boto3.client('events', region_name='us-east-1')

BUS_NAME = 'orders-bus'

def process_payment(order):
    """Simulate payment processing — 80% success rate."""
    time.sleep(0.1)  # simulate API call
    return random.random() > 0.2  # 80% success

def lambda_handler(event, context):
    """
    SQS triggers Lambda with a batch of records.
    We must return which records failed so SQS can retry only those.
    """
    failed_records = []
    
    for record in event['Records']:
        order = json.loads(record['body'])
        order_id = order['order_id']
        
        print(f"Processing order {order_id}")
        
        success = process_payment(order)
        
        # Publish outcome to EventBridge
        # EventBridge will route this event based on the 'status' field
        detail = {
            'order_id': order_id,
            'user_id': order['user_id'],
            'total': order['total'],
            'status': 'completed' if success else 'failed',
            'processed_at': int(time.time())
        }
        
        events_client.put_events(Entries=[{
            'EventBusName': BUS_NAME,
            'Source': 'orders.processor',
            'DetailType': 'OrderProcessed',
            'Detail': json.dumps(detail)
        }])
        
        if not success:
            # Return this record as failed so SQS keeps it and retries
            # After maxReceiveCount (3) failures, SQS sends it to DLQ
            failed_records.append({'itemIdentifier': record['messageId']})
            print(f"Order {order_id} FAILED — will be retried by SQS")
        else:
            print(f"Order {order_id} COMPLETED successfully")
    
    # SQS partial batch response: only failed records are retried
    return {'batchItemFailures': failed_records}
```

**Deploy:**

```bash
zip order_processor.zip order_processor.py

aws lambda create-function \
  --function-name order-processor \
  --runtime python3.12 \
  --role <ROLE_ARN> \
  --handler order_processor.lambda_handler \
  --zip-file fileb://order_processor.zip \
  --timeout 60

# Create the SQS event source mapping
# This makes Lambda poll SQS automatically
aws lambda create-event-source-mapping \
  --function-name order-processor \
  --event-source-arn <ORDERS_QUEUE_ARN> \
  --batch-size 5 \
  --function-response-types ReportBatchItemFailures
```

> `ReportBatchItemFailures` is critical — it allows Lambda to tell SQS which specific records in the batch failed, so only those are retried (not the whole batch).

---

### Lambda 3: order-notification (EventBridge Target)

Triggered when an order is **completed**. Sends a confirmation "email".

**File: `lambda/order_notification.py`**

```python
import json

def lambda_handler(event, context):
    """
    Triggered by EventBridge when detail.status = 'completed'.
    In a real system, this would call SES to send an email.
    """
    order = event['detail']
    
    print(f"Sending confirmation email for order {order['order_id']}")
    print(f"To: user {order['user_id']}")
    print(f"Amount: ${order['total']}")
    print(f"Email body: 'Your order {order['order_id']} has been confirmed!'")
    
    return {'status': 'email_sent', 'order_id': order['order_id']}
```

**Deploy:**

```bash
zip order_notification.zip order_notification.py

aws lambda create-function \
  --function-name order-notification \
  --runtime python3.12 \
  --role <ROLE_ARN> \
  --handler order_notification.lambda_handler \
  --zip-file fileb://order_notification.zip \
  --timeout 30
```

---

### Lambda 4: retry-alert (EventBridge Target)

Triggered when an order **fails**. Alerts the operations team.

**File: `lambda/retry_alert.py`**

```python
import json

def lambda_handler(event, context):
    """
    Triggered by EventBridge when detail.status = 'failed'.
    SQS will retry the original job up to maxReceiveCount (3) times.
    This Lambda just alerts the team immediately on any failure.
    """
    order = event['detail']
    
    print(f"ALERT: Order {order['order_id']} failed payment processing")
    print(f"User: {order['user_id']} — Amount: ${order['total']}")
    print("SQS will retry this order. Ops team notified.")
    
    # In production: call SNS to send SMS/Slack/PagerDuty alert
    
    return {'status': 'alert_sent', 'order_id': order['order_id']}
```

**Deploy:**

```bash
zip retry_alert.zip retry_alert.py

aws lambda create-function \
  --function-name retry-alert \
  --runtime python3.12 \
  --role <ROLE_ARN> \
  --handler retry_alert.lambda_handler \
  --zip-file fileb://retry_alert.zip \
  --timeout 30
```

---

### Lambda 5: analytics (Kinesis Consumer)

Triggered by every batch of records from the Kinesis clickstream. Computes real-time metrics.

**File: `lambda/analytics.py`**

```python
import json
import boto3
import base64
from datetime import datetime
from collections import defaultdict

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('clickstream-metrics')

def lambda_handler(event, context):
    """
    Kinesis triggers Lambda with a batch of records from one or more shards.
    Each record's Data is base64-encoded by Kinesis — we must decode it.
    Records within a shard are in order (guaranteed by Kinesis).
    """
    event_counts = defaultdict(int)
    total_revenue = 0.0
    
    for record in event['Records']:
        # Kinesis encodes data as base64
        payload = json.loads(base64.b64decode(record['kinesis']['data']).decode('utf-8'))
        
        shard_id = record['eventID'].split(':')[0]
        sequence = record['kinesis']['sequenceNumber']
        
        print(f"Shard: {shard_id} | Seq: {sequence[-8:]} | Event: {payload['event_type']} | User: {payload['user_id']}")
        
        event_counts[payload['event_type']] += 1
        
        if payload['event_type'] == 'order_placed':
            total_revenue += payload.get('total', 0)
    
    # Write aggregated metrics to DynamoDB
    timestamp = datetime.utcnow().isoformat()
    
    for event_type, count in event_counts.items():
        table.put_item(Item={
            'metric_key': f'count#{event_type}',
            'timestamp': timestamp,
            'count': count,
            'batch_size': len(event['Records'])
        })
    
    if total_revenue > 0:
        table.put_item(Item={
            'metric_key': 'revenue#batch',
            'timestamp': timestamp,
            'amount': str(total_revenue),
            'orders_in_batch': event_counts.get('order_placed', 0)
        })
    
    print(f"Processed {len(event['Records'])} records | Events: {dict(event_counts)} | Revenue: ${total_revenue:.2f}")
    
    return {'processed': len(event['Records'])}
```

**Deploy:**

```bash
zip analytics.zip analytics.py

aws lambda create-function \
  --function-name analytics \
  --runtime python3.12 \
  --role <ROLE_ARN> \
  --handler analytics.lambda_handler \
  --zip-file fileb://analytics.zip \
  --timeout 60

# Create the Kinesis event source mapping
# Lambda will poll both shards and process records in batches
aws lambda create-event-source-mapping \
  --function-name analytics \
  --event-source-arn <KINESIS_STREAM_ARN> \
  --batch-size 100 \
  --starting-position LATEST \
  --bisect-batch-on-function-error
```

> `bisect-batch-on-function-error`: if a batch fails, Lambda splits it in half and retries each half separately — helps isolate a single bad record instead of blocking the entire shard.

---

## Step 7 — Create the EventBridge Rules

These rules are the core of EventBridge's value: **content-based routing** based on what's inside the event.

### 7a. Add Lambda permission to be invoked by EventBridge

```bash
aws lambda add-permission \
  --function-name order-notification \
  --statement-id eventbridge-invoke \
  --action lambda:InvokeFunction \
  --principal events.amazonaws.com

aws lambda add-permission \
  --function-name retry-alert \
  --statement-id eventbridge-invoke \
  --action lambda:InvokeFunction \
  --principal events.amazonaws.com
```

### 7b. Rule 1 — Route completed orders to notification Lambda

```bash
aws events put-rule \
  --name route-completed-orders \
  --event-bus-name orders-bus \
  --event-pattern '{
    "source": ["orders.processor"],
    "detail-type": ["OrderProcessed"],
    "detail": {
      "status": ["completed"]
    }
  }' \
  --state ENABLED

aws events put-targets \
  --rule route-completed-orders \
  --event-bus-name orders-bus \
  --targets '[{
    "Id": "notification-lambda",
    "Arn": "<ORDER_NOTIFICATION_LAMBDA_ARN>"
  }]'
```

**Observe the event pattern:** EventBridge filters on `detail.status = "completed"` — only events with this exact value match. The `order-processor` Lambda publishes to the same bus for both completed and failed orders, but this rule only matches completed ones.

### 7c. Rule 2 — Route failed orders to alert Lambda

```bash
aws events put-rule \
  --name route-failed-orders \
  --event-bus-name orders-bus \
  --event-pattern '{
    "source": ["orders.processor"],
    "detail-type": ["OrderProcessed"],
    "detail": {
      "status": ["failed"]
    }
  }' \
  --state ENABLED

aws events put-targets \
  --rule route-failed-orders \
  --event-bus-name orders-bus \
  --targets '[{
    "Id": "retry-alert-lambda",
    "Arn": "<RETRY_ALERT_LAMBDA_ARN>"
  }]'
```

---

## Step 8 — Test the Pipeline

### Test 1 — Trigger a successful order

```bash
aws lambda invoke \
  --function-name order-producer \
  --payload '{"user_id": "user-123", "items": [{"sku": "SHOE-42", "qty": 1}], "total": 149.99}' \
  --cli-binary-format raw-in-base64-out \
  output.json && cat output.json
```

**Expected chain of events:**
1. `order-producer` puts a message on SQS and a record on Kinesis
2. SQS triggers `order-processor` (within ~1s)
3. `order-processor` processes the order and publishes an `OrderProcessed` event to EventBridge
4. If `status=completed`: EventBridge routes to `order-notification` Lambda
5. If `status=failed`: EventBridge routes to `retry-alert` Lambda; SQS retries the original job
6. `analytics` Lambda processes the Kinesis record independently

### Test 2 — Send multiple orders and observe

```bash
# Send 10 orders rapidly
for i in {1..10}; do
  aws lambda invoke \
    --function-name order-producer \
    --payload "{\"user_id\": \"user-$((RANDOM % 5 + 1))\", \"total\": $((RANDOM % 200 + 10))}" \
    --cli-binary-format raw-in-base64-out \
    /dev/null
  echo "Order $i sent"
done
```

### Test 3 — Check CloudWatch Logs

```bash
# View order-processor logs (see SQS batch processing)
aws logs tail /aws/lambda/order-processor --follow

# View analytics logs (see Kinesis shard/sequence info)
aws logs tail /aws/lambda/analytics --follow

# View notification logs (see EventBridge routing)
aws logs tail /aws/lambda/order-notification --follow
```

### Test 4 — Query the DynamoDB metrics table

```bash
aws dynamodb scan --table-name clickstream-metrics
```

### Test 5 — Check the Dead Letter Queue

After sending many orders, some will fail (80% success rate). After 3 failures, those orders move to the DLQ:

```bash
aws sqs get-queue-attributes \
  --queue-url <DLQ_URL> \
  --attribute-names ApproximateNumberOfMessages
```

---

## Concepts reinforced by this lab

### Why SQS for order jobs?
- **Durability**: the order is stored in SQS — even if the payment processor goes down for 10 minutes, no orders are lost
- **Retry with Visibility Timeout**: failed processing attempts are automatically retried without any extra code
- **DLQ**: poison-pill orders that keep failing don't block the queue — they move to the DLQ for manual inspection
- **Backpressure**: during peak load, orders queue up safely — Lambda processes at its own pace

### Why EventBridge for routing?
- `order-processor` doesn't need to know about `order-notification` or `retry-alert` — it just publishes to the bus
- Adding a new action (e.g., a loyalty points Lambda) requires only a new EventBridge rule, zero code changes to `order-processor`
- The routing logic (`status=completed` vs `status=failed`) lives in EventBridge, not in application code

### Why Kinesis for clickstream?
- `order-producer` AND any other producer can send to the stream independently
- `analytics` Lambda is a completely independent consumer — it doesn't affect SQS or EventBridge at all
- If `analytics` has a bug, you can **replay** the last 24 hours of Kinesis data after the fix — impossible with SQS
- The `user_id` partition key ensures all events from the same user land on the same shard in order

---

## Cleanup

Run these commands to avoid incurring AWS charges:

```bash
# Delete Lambda functions
for fn in order-producer order-processor order-notification retry-alert analytics; do
  aws lambda delete-function --function-name $fn
done

# Delete SQS queues
aws sqs delete-queue --queue-url <ORDERS_QUEUE_URL>
aws sqs delete-queue --queue-url <DLQ_URL>

# Delete Kinesis stream
aws kinesis delete-stream --stream-name clickstream

# Delete EventBridge rules and bus
aws events remove-targets --rule route-completed-orders --event-bus-name orders-bus --ids notification-lambda
aws events remove-targets --rule route-failed-orders --event-bus-name orders-bus --ids retry-alert-lambda
aws events delete-rule --name route-completed-orders --event-bus-name orders-bus
aws events delete-rule --name route-failed-orders --event-bus-name orders-bus
aws events delete-event-bus --name orders-bus

# Delete DynamoDB table
aws dynamodb delete-table --table-name clickstream-metrics

# Detach and delete IAM role
aws iam detach-role-policy --role-name lab04-lambda-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam detach-role-policy --role-name lab04-lambda-role --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess
aws iam detach-role-policy --role-name lab04-lambda-role --policy-arn arn:aws:iam::aws:policy/AmazonKinesisFullAccess
aws iam detach-role-policy --role-name lab04-lambda-role --policy-arn arn:aws:iam::aws:policy/AmazonEventBridgeFullAccess
aws iam detach-role-policy --role-name lab04-lambda-role --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
aws iam delete-role --role-name lab04-lambda-role
```

---

## Architecture decision cheatsheet

Use this to quickly decide which service to reach for:

```
Is this a task to be processed by one worker?
  YES → SQS (queue, retry, DLQ, backpressure)

Is this an event that should trigger different actions based on its content?
  YES → EventBridge (rules, patterns, fan-out, no code coupling)

Is this a high-volume continuous stream of data with multiple consumers?
  YES → Kinesis Data Streams (replay, shards, ordered per partition key)

Do I just want to deliver data to S3/Redshift/OpenSearch?
  YES → Kinesis Firehose (fully managed, near real-time, no code)

Do I want to push the same notification to many subscribers at once?
  YES → SNS (pub-sub, mobile push, email, SMS)
```
