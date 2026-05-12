import json
import boto3
import base64
import os
from datetime import datetime
from collections import defaultdict

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table(os.environ.get('METRICS_TABLE', 'clickstream-metrics'))


def lambda_handler(event, context):
    """
    Triggered by Kinesis Data Streams event source mapping.

    Kinesis concepts demonstrated:
    - Lambda receives a BATCH of records from one or more shards.
    - Each record's Data field is base64-encoded — we must decode it.
    - Records from the same shard arrive in ORDER (sequenceNumber is monotonic).
    - The 'eventID' tells us which shard the record came from.
    - Records from different shards may be interleaved in the batch.

    Lambda + Kinesis behavior:
    - Lambda polls each shard at its own pace (one concurrent invocation per shard).
    - If this function throws an exception, Lambda retries the ENTIRE batch from
      the same position in the shard until it succeeds or the record expires.
    - bisect-batch-on-function-error splits the batch on failure, isolating bad records.
    """
    event_counts = defaultdict(int)
    total_revenue = 0.0
    shard_summary = defaultdict(int)

    for record in event['Records']:
        # Kinesis encodes data as base64 — always decode before parsing
        raw_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        payload = json.loads(raw_data)

        # Each record has a shard ID embedded in the eventID
        shard_id = record['eventID'].split(':')[0]
        sequence = record['kinesis']['sequenceNumber']
        partition_key = record['kinesis']['partitionKey']  # = user_id in our case

        print(
            f"[Kinesis] Shard: {shard_id} | "
            f"Seq: ...{sequence[-8:]} | "
            f"PartitionKey (user): {partition_key} | "
            f"Event: {payload['event_type']}"
        )

        event_counts[payload['event_type']] += 1
        shard_summary[shard_id] += 1

        if payload['event_type'] == 'order_placed':
            total_revenue += float(payload.get('total', 0))

    # Aggregate metrics for this batch and persist to DynamoDB
    timestamp = datetime.utcnow().isoformat()
    batch_size = len(event['Records'])

    for event_type, count in event_counts.items():
        table.put_item(Item={
            'metric_key': f'count#{event_type}',
            'timestamp': timestamp,
            'count': count,
            'batch_size': batch_size,
        })

    if total_revenue > 0:
        table.put_item(Item={
            'metric_key': 'revenue#batch',
            'timestamp': timestamp,
            'amount': str(round(total_revenue, 2)),
            'orders_in_batch': event_counts.get('order_placed', 0),
        })

    print(
        f"[Kinesis] Batch complete — "
        f"Records: {batch_size} | "
        f"Events: {dict(event_counts)} | "
        f"Revenue: ${total_revenue:.2f} | "
        f"Shards in batch: {dict(shard_summary)}"
    )

    return {'processed_records': batch_size}
