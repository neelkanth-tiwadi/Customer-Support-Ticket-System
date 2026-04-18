def get_ticket_input():
    while True:
        text = input("Enter support ticket: ").strip()
        if len(text) < 5 or text.isdigit():
           print("Invalid ticket. Enter meaningful text.")
        else:
            return text