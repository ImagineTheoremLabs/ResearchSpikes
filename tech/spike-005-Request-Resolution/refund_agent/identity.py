import json


def load_customers():
    with open("../samples/customers.json", "r") as file:
        return json.load(file)


def verify_identity(order_id, email):
    customers = load_customers()

    # Find customer by email
    customer = next((c for c in customers if c["email"] == email), None)

    if not customer:
        return False, "Customer email not found"

    # Now verify order ownership
    from orders import get_order
    order, _ = get_order(order_id)

    if not order:
        return False, "Order not found"

    if order["customer_id"] != customer["customer_id"]:
        return False, "Order does not belong to this email"

    return True, f"Identity verified for {customer['name']}"
