1.User Input
  The user enters a customer support ticket in text format using a Python‑based interface.

2.Text Pre‑processing
  The input text is cleaned and prepared for analysis (lowercasing, removing unnecessary characters).

3.Feature Extraction
  The processed text is converted into numerical features using the TF‑IDF technique.

4.Machine Learning Prediction
  A trained classification model predicts:
  Ticket category
  Ticket priority
  Prediction confidence score

5.Decision Logic
  The system applies rule‑based logic:
  High confidence → auto‑resolution
  Low confidence → assign to human agent

6.Response Generation
  For auto‑resolvable tickets, a predefined response is generated based on the predicted category.

7.Output Display
 The final result is shown to the user, including:
 Ticket category
 Priority
 Confidence score
 Resolution or assignment message