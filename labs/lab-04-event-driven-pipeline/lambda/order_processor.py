import json
import boto3
import random
import time
import os

events_client = boto3.client('events', region_name='us-east-1')

BUS_NAME = os.environ.get('BUS_NAME', 'orders-bus')


def process_payment(order: dict) -> bool:
    """Simulate payment processing — 80% success rate."""
    time.sleep(0.1)  # simulate external API call latency
    return random.random() > 0.2


def lambda_handler(event, context):
    """
    SQS triggers Lambda with a batch of up to `batch-size` records.

    Key SQS concepts demonstrated here:
    - Lambda polls SQS automatically (event source mapping)
    - We return `batchItemFailures` so SQS retries ONLY failed records,
      not the whole batch (requires ReportBatchItemFailures response type)
    - Successfully processed records are automatically deleted by SQS
    - Failed records stay invisible until Visibility Timeout expires,
      then reappear for retry — up to maxReceiveCount before going to DLQ
    """
    failed_records = []

    for record in event['Records']:
        order = json.loads(record['body'])
        order_id = order['order_id']
        receive_count = int(record['attributes'].get('ApproximateReceiveCount', 1))

        print(f"[SQS] Processing order {order_id} (attempt #{receive_count})")

        success = process_payment(order)

        # Publish outcome event to EventBridge custom bus.
        # EventBridge routes this event based on detail.status —
        # the processor does NOT need to know who handles each outcome.
        detail = {
            'order_id': order_id,
            'user_id': order['user_id'],
            'total': order['total'],
            'status': 'completed' if success else 'failed',
            'attempt': receive_count,
            'processed_at': int(time.time()),
        }

        events_client.put_events(Entries=[{
            'EventBusName': BUS_NAME,
            'Source': 'orders.processor',
            'DetailType': 'OrderProcessed',
            'Detail': json.dumps(detail),
        }])

        if not success:
            print(f"[SQS] Order {order_id} FAILED (attempt {receive_count}) — returning to queue for retry")
            # Returning the messageId tells SQS to keep this message.
            # After maxReceiveCount failures it will go to the DLQ.
            failed_records.append({'itemIdentifier': record['messageId']})
        else:
            print(f"[SQS] Order {order_id} COMPLETED — message will be deleted from queue")

    # SQS partial batch response: only failed records are retried.
    # Records NOT in this list are automatically deleted.
    return {'batchItemFailures': failed_records}
