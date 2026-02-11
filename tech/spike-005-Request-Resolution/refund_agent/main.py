import json
import os

from identity import verify_identity
from orders import get_order
from policy import evaluate_refund_policy
from refund import execute_refund


def save_decision_log(filename, data):
    os.makedirs("../logs", exist_ok=True)
    with open(f"../logs/{filename}", "w") as file:
        json.dump(data, file, indent=4)


def save_transcript(filename, content):
    os.makedirs("../assets", exist_ok=True)
    with open(f"../assets/{filename}", "w") as file:
        file.write(content)


def run_trial(order_id, email, trial_name):
    print(f"\n--- Running {trial_name} ---")

    # Step 1: Identity Verification
    identity_verified, identity_msg = verify_identity(order_id, email)
    print(identity_msg)

    if not identity_verified:
        print("Identity verification failed.")
        return

    # Step 2: Fetch Order
    order, order_msg = get_order(order_id)
    print(order_msg)

    if not order:
        print("Order retrieval failed.")
        return

    # Step 3: Evaluate Policy
    status, policy_msg = evaluate_refund_policy(order)
    print(policy_msg)

    decision_log = {
        "order_id": order_id,
        "identity_verified": identity_verified,
        "policy_status": status,
        "policy_message": policy_msg
    }

    transcript = f"""
Agent: Please provide your order ID.
Customer: {order_id}
Agent: Please confirm your email.
Customer: {email}
Agent: {policy_msg}
"""

    # Step 4: Handle Refund Logic
    if status == "FULL":
        receipt = execute_refund(order)
        decision_log["refund"] = receipt
        transcript += f"\nAgent: Your full refund of ₹{receipt['amount']} has been processed.\n"
        print("Full refund processed successfully.")

    elif status == "PARTIAL":
        partial_amount = round(order["amount"] * 0.5, 2)
        receipt = execute_refund(order)
        receipt["amount"] = partial_amount
        decision_log["refund"] = receipt
        transcript += f"\nAgent: You are eligible for a 50% refund of ₹{partial_amount}.\n"
        print("Partial refund processed successfully.")

    else:
        transcript += "\nAgent: Unfortunately, your refund request has been denied.\n"
        print("Refund denied.")

    # Save artifacts
    save_decision_log(f"{trial_name}_decision_log.json", decision_log)
    save_transcript(f"{trial_name}_transcript.txt", transcript)

    print(f"{trial_name} completed.\n")


if __name__ == "__main__":
    # Trial A → Full Refund
    run_trial("ORD101", "rahul@example.com", "Trial_A")

    # Trial B → Denied
    run_trial("ORD102", "ananya@example.com", "Trial_B")

    # Trial C → Partial Refund
    run_trial("ORD103", "rahul@example.com", "Trial_C")
