from .decision_engine import decide_action
from .response_templates import get_response
from src.models.predict import model_predict

def process_ticket(ticket: str):
    category, confidence = model_predict(ticket)
    action = decide_action(confidence)
    if action == "AUTO_RESOLVE":
        priority = "Low"
        response = get_response(category)
    else:
        priority = "High"
        response = "Ticket assigned to support agent."

    return {
        "category": category,
        "priority": priority,
        "confidence": round(confidence,2),
        "action": action,
        "response": response
    }



if __name__ == "__main__":
    ticket = "I cannot login to my account"
    category = "Login Issue"
    confidence = 0.8

    result = process_ticket(ticket, category, confidence)

    for k, v in result.items():
        print(f"{k}: {v}")