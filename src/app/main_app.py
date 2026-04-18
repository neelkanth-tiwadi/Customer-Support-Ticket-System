from .input_handler import get_ticket_input
from .output_formatter import format_output
from ..pipeline import process_ticket

def main():
    try:
        ticket = get_ticket_input()

        if ticket is None:
            return

        
        from ..models.predict import model_predict
        category, confidence = model_predict(ticket)

        result = process_ticket(ticket, category, confidence)
        format_output(result)

    except Exception as e:
        print("An error occurred while processing the ticket.")
        print("Error:", e)

if __name__ == "__main__":
    main()