import uuid
from datetime import datetime


def execute_refund(order):
    """
    Simulates refund execution.
    Returns refund details.
    """

    refund_id = f"RF-{uuid.uuid4().hex[:8].upper()}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    receipt = {
        "refund_id": refund_id,
        "order_id": order["order_id"],
        "amount": order["amount"],
        "method": "Original Payment Method",
        "processed_at": timestamp
    }

    return receipt
