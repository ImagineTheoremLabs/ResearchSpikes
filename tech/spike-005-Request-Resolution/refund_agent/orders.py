import json


def load_orders():
    with open("../samples/orders.json", "r") as file:
        return json.load(file)


def get_order(order_id):
    orders = load_orders()

    order = next((o for o in orders if o["order_id"] == order_id), None)

    if not order:
        return None, "Order not found"

    return order, "Order retrieved successfully"
