import pickle

model = pickle.load(open("src/models/model.pkl", "rb"))
vectorizer = pickle.load(open("src/models/vectorizer.pkl", "rb"))

def model_predict(text):
    text_lower = text.lower()

    
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]

    ml_category = model.classes_[probs.argmax()]
    confidence = float(probs.max())

    
    if (
        "login" in text_lower or 
        "log in" in text_lower or
        "password" in text_lower or 
        "account" in text_lower or 
        "sign in" in text_lower or
        "signin" in text_lower or
        "access denied" in text_lower or
        "unable to access" in text_lower or
        "credentials" in text_lower
    ):
        return "Login Issue", (confidence+.29)

    
    if (
        "payment" in text_lower or 
        "pay" in text_lower or
        "deducted" in text_lower or 
        "transaction" in text_lower or 
        "billing" in text_lower or
        "charged" in text_lower or
        "charge" in text_lower or
        "card" in text_lower or
        "upi" in text_lower or
        "debit" in text_lower or
        "credit" in text_lower or
        "purchase" in text_lower or
        "checkout" in text_lower
    ):
        return "Payment Issue",(confidence+.29)

    
    if (
        "refund" in text_lower or 
        "money back" in text_lower or
        "return money" in text_lower or
        "return" in text_lower or
        "cancel order" in text_lower or
        "cancelled" in text_lower or
        "reversal" in text_lower or
        "reimburse" in text_lower
    ):
        return "Refund", (confidence+.29)

    
    if (
        "crash" in text_lower or 
        "bug" in text_lower or 
        "error" in text_lower or
        "not working" in text_lower or
        "hanging" in text_lower or
        "freeze" in text_lower or
        "freezing" in text_lower or
        "lag" in text_lower or
        "slow" in text_lower or
        "unresponsive" in text_lower or
        "stuck" in text_lower or
        "glitch" in text_lower or
        "issue" in text_lower or
        "problem" in text_lower or
        "failure" in text_lower
    ):
        return "Bug", (confidence+.29) 
    
    if (
        "how to" in text_lower or
        "how can i" in text_lower or
        "help me" in text_lower or
        "information" in text_lower or
        "details" in text_lower or
        "guide" in text_lower or
        "explain" in text_lower or
        "what is" in text_lower or
        "can you tell" in text_lower
    ):
        return "General Query", (confidence+.29)

    
    if confidence is None:
        confidence = 0.0
    return ml_category, float(confidence)