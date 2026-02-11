import re
from datetime import datetime

from identity import verify_identity
from orders import get_order
from policy import evaluate_refund_policy
from refund import execute_refund


def extract_order_id(text):
    match = re.search(r"ORD\d+", text)
    return match.group(0) if match else None


def extract_email(text):
    match = re.search(r"\S+@\S+\.\S+", text)
    return match.group(0) if match else None


def process_user_request(user_text):
    order_id = extract_order_id(user_text)
    email = extract_email(user_text)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    decision_log = {
        "timestamp": timestamp,
        "user_input": user_text,
        "order_id": order_id,
        "email": email
    }

    if not order_id or not email:
        decision_log["status"] = "ERROR"
        decision_log["message"] = "Missing order ID or email"
        return "I’m sorry, I couldn’t identify your order ID or email. Please provide both.", decision_log

    identity_verified, identity_msg = verify_identity(order_id, email)

    if not identity_verified:
        decision_log["status"] = "IDENTITY_FAILED"
        decision_log["message"] = identity_msg
        return f"Identity verification failed: {identity_msg}", decision_log

    order, order_msg = get_order(order_id)

    if not order:
        decision_log["status"] = "ORDER_NOT_FOUND"
        decision_log["message"] = "Order not found"
        return "I couldn’t find your order.", decision_log

    status, policy_msg = evaluate_refund_policy(order)
    decision_log["policy_status"] = status
    decision_log["policy_message"] = policy_msg

    if status == "FULL":
        receipt = execute_refund(order)
        decision_log["refund"] = receipt
        return f"{policy_msg}. Your full refund of ₹{receipt['amount']} has been processed.", decision_log

    elif status == "PARTIAL":
        partial_amount = round(order["amount"] * 0.5, 2)
        receipt = execute_refund(order)
        receipt["amount"] = partial_amount
        decision_log["refund"] = receipt
        return f"{policy_msg}. You will receive ₹{partial_amount} as a partial refund.", decision_log

    else:
        decision_log["status"] = "DENIED"
        return f"{policy_msg}. Unfortunately, your refund cannot be processed.", decision_log
