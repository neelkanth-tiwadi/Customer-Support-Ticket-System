RESPONSES = {
    "Login Issue": "Please reset your password using the forgot password option.",
    "Payment Issue": "Please verify your payment details and try again.",
    "Bug": "Our team has been notified about the issue.",
    "General Query": "Thank you for contacting support."
}


def get_response(category):
    return RESPONSES.get(category, "Your ticket has been sent to support.")