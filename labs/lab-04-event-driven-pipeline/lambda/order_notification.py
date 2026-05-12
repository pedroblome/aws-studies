import json


def lambda_handler(event, context):
    """
    Triggered by EventBridge rule: source=orders.processor AND detail.status=completed.

    EventBridge concept demonstrated:
    - Content-based routing: this Lambda is only invoked when status='completed'
    - The event schema from EventBridge wraps our detail inside the standard envelope:
        event['source']      = 'orders.processor'
        event['detail-type'] = 'OrderProcessed'
        event['detail']      = our custom payload
    - order-processor had zero knowledge of this Lambda — it just published to the bus.
      Adding this consumer required only a new EventBridge rule, no code change.
    """
    order = event['detail']

    print(f"[EventBridge → Notification] Order COMPLETED: {order['order_id']}")
    print(f"  User:    {order['user_id']}")
    print(f"  Amount:  ${order['total']:.2f}")
    print(f"  Attempt: #{order['attempt']}")

    # In a real system: call Amazon SES to send a confirmation email
    email_body = (
        f"Hi! Your order {order['order_id']} has been confirmed. "
        f"Total charged: ${order['total']:.2f}. Thank you for your purchase!"
    )
    print(f"  [SES] Sending email: {email_body}")

    return {
        'status': 'email_sent',
        'order_id': order['order_id'],
    }
