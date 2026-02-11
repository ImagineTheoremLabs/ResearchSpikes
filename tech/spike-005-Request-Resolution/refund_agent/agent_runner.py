import json
import os
from datetime import datetime
from llm_agent import process_user_request, extract_order_id, extract_email


def save_llm_log(log_data):
    os.makedirs("../logs", exist_ok=True)
    filepath = "../logs/LLM_session_log.json"

    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            existing_logs = json.load(f)
    else:
        existing_logs = []

    existing_logs.append(log_data)

    with open(filepath, "w") as f:
        json.dump(existing_logs, f, indent=4)


def save_transcript_line(text):
    os.makedirs("../assets", exist_ok=True)
    filepath = "../assets/LLM_transcript.txt"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {text}\n")


if __name__ == "__main__":
    print("🤖 Refund Resolution Voice Agent (Simulated LLM)")
    print("Type your request below. Type 'exit' to quit.\n")

    session_state = {
        "order_id": None,
        "email": None
    }

    while True:
        user_input = input("Customer: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Thank you for contacting support. Goodbye!")
            save_transcript_line("Agent: Session ended.")
            break

        save_transcript_line(f"Customer: {user_input}")

        # Try extracting info from user input
        extracted_order = extract_order_id(user_input)
        extracted_email = extract_email(user_input)

        if extracted_order:
            session_state["order_id"] = extracted_order

        if extracted_email:
            session_state["email"] = extracted_email

        # Ask for missing information
        if not session_state["order_id"]:
            response = "Could you please provide your order ID?"
            print(f"Agent: {response}\n")
            save_transcript_line(f"Agent: {response}")
            continue

        if not session_state["email"]:
            response = "Please provide the email associated with the order."
            print(f"Agent: {response}\n")
            save_transcript_line(f"Agent: {response}")
            continue

        # If both collected → process request
        combined_input = f"{session_state['order_id']} {session_state['email']}"
        response, decision_log = process_user_request(combined_input)

        print(f"Agent: {response}\n")

        save_transcript_line(f"Agent: {response}")
        save_llm_log(decision_log)

        # Reset session for next request
        session_state = {
            "order_id": None,
            "email": None
        }
