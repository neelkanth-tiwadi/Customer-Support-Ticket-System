from flask import Flask, render_template, request, redirect, url_for
from src.pipeline import process_ticket
from web_app.email_utils import send_email
app = Flask(__name__)


last_result = None

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        ticket = request.form.get("ticket")
        email = request.form.get("email")

        if ticket and email:
            result = process_ticket(ticket)

            # 👇 send email after processing
            send_email(email, ticket, result)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)