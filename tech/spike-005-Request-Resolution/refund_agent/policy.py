from datetime import datetime


REFUND_WINDOW_DAYS = 30


def is_within_refund_window(order_date_str):
    order_date = datetime.strptime(order_date_str, "%Y-%m-%d")
    today = datetime.now()
    delta = today - order_date
    return delta.days <= REFUND_WINDOW_DAYS


def evaluate_refund_policy(order):
    """
    Returns:
        status: "FULL", "PARTIAL", or "DENIED"
        message: explanation string
    """

    if not order["delivered"]:
        return "DENIED", "Order not delivered"

    if order["promotional"]:
        return "DENIED", "Promotional items are non-refundable"

    if not is_within_refund_window(order["order_date"]):
        return "DENIED", "Order exceeds 30-day refund window"

    if order["amount"] > 500:
        return "PARTIAL", "Eligible for 50% refund due to restocking policy"

    return "FULL", "Eligible for full refund"
