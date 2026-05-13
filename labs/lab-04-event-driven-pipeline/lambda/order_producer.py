import json
import boto3
import uuid
import time
import os

sqs = boto3.client("sqs", region_name="us-east-1")
kinesis = boto3.client("kinesis", region_name="us-east-1")

QUEUE_URL = os.environ["QUEUE_URL"]
STREAM_NAME = "clickstream"


# event is the payload that triggers the Lambda -> in this case simulates a post order in a ecommerce app
def lambda_handler(event, context):
    order_id = str(uuid.uuid4())
    user_id = event.get("user_id", "user-001")

    # 1. Send order job to SQS for reliable async processing.
    #    SQS guarantees delivery and handles retries via Visibility Timeout.
    order_payload = {
        "order_id": order_id,
        "user_id": user_id,
        "items": event.get("items", []),
        "total": event.get("total", 0),
        "order_type": event.get("order_type", "standard"),
        "created_at": int(time.time()),
    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order_payload),
        MessageAttributes={
            "order_type": {
                "DataType": "String",
                "StringValue": order_payload["order_type"],
            }
        },
    )
    print(f"[SQS] Order {order_id} queued for processing")

    # 2. Send clickstream event to Kinesis for real-time analytics.
    #    partition_key = user_id ensures all events from the same user
    #    land on the same shard (ordered per user).
    kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(
            {
                "event_type": "order_placed",
                "user_id": user_id,
                "order_id": order_id,
                "total": order_payload["total"],
                "timestamp": int(time.time()),
            }
        ),
        PartitionKey=user_id,
    )
    print(f"[Kinesis] Clickstream event sent for user {user_id}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Order received and queued",
                "order_id": order_id,
            }
        ),
    }
