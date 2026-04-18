CONFIDENCE_THRESHOLD = 0.7


def decide_action(confidence):
    if confidence >= CONFIDENCE_THRESHOLD:
        return "AUTO_RESOLVE"
    return "ASSIGNED_TO_AGENT"


if __name__ == "__main__":
    confidence = 0.7
    decision = decide_action(confidence)
    print("Confidence:", confidence)
    print("Decision:", decision)