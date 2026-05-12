import json


def lambda_handler(event, context):
    """
    Triggered by EventBridge rule: source=orders.processor AND detail.status=failed.

    EventBridge concept demonstrated:
    - Same bus, different rule → different target.
    - Two rules on the same bus pattern, each matching a different status value.
    - Neither rule interferes with the other.

    Note on the two-layer retry strategy:
    - SQS will retry the original order job up to maxReceiveCount (3) times.
      Each retry goes through order-processor again.
    - This Lambda fires on EVERY failure attempt, giving the ops team
      immediate visibility without waiting for the DLQ.
    - The DLQ acts as the final safety net for orders that exhaust all retries.
    """
    order = event['detail']

    print(f"[EventBridge → Alert] Order FAILED: {order['order_id']}")
    print(f"  User:    {order['user_id']}")
    print(f"  Amount:  ${order['total']:.2f}")
    print(f"  Attempt: #{order['attempt']} (SQS will retry up to 3 times before DLQ)")

    alert_message = (
        f"PAYMENT FAILURE — Order {order['order_id']} failed on attempt #{order['attempt']}. "
        f"User: {order['user_id']}. Amount: ${order['total']:.2f}. "
        f"SQS will retry. Check DLQ if this keeps failing."
    )
    print(f"  [SNS/Slack] Sending alert: {alert_message}")

    # In a real system: publish to an SNS topic that fans out to
    # Slack (via Lambda), PagerDuty (HTTP endpoint), and email.

    return {
        'status': 'alert_sent',
        'order_id': order['order_id'],
        'attempt': order['attempt'],
    }
