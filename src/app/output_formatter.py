def format_output(result):
    print("\n--- Ticket Analysis Result ---")
    print("Category :", result["category"])
    print("Priority :", result["priority"])
    print("Confidence :", round(result["confidence"],2))
    print("Action :", result["action"])
    print("Response :", result["response"])