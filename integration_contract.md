Function: process_ticket

Location: src/pipeline.py

Signature:
process_ticket(ticket: str, category: str, confidence: float)

Returns:
decision (str)
response (str)

Rules:
- category must be a string label
- confidence must be between 0 and 1
- No one changes this function without approval