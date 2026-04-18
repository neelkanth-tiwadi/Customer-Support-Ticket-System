import smtplib
from email.mime.text import MIMEText

def send_email(user_email, ticket, result):
    sender_email = "n2323422@gmail.com"
    sender_password = "nihf sapk vefd dpnu"

    subject = "Your Support Ticket Update"

    body = f"""
    Thank you for contacting support.

    Your Issue:
    {ticket}

    Category: {result['category']}
    Priority: {result['priority']}
    Response: {result['response']}

    We will get back to you if needed.

    Regards,
    Support Team
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = user_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, user_email, msg.as_string())
        server.quit()
        print("Email sent successfully")

    except Exception as e:
        print("Email error:", e)