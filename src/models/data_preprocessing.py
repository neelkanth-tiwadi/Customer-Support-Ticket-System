import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import os



def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)  
    text = re.sub(r'\s+', ' ', text).strip()
    return text



def load_data():
    base = os.path.dirname(__file__)        
    path = os.path.join(base, "..", "data", "dataset.csv")

    df = pd.read_csv(path)
   
      
    df["combined_text"] = (
    (df["Ticket Subject"].fillna('') + " ") * 3 +
    df["Ticket Description"].fillna('')
    )

    df["clean_text"] = df["combined_text"].apply(clean_text)
    df["label"] = df["Ticket Type"].apply(simplify_label)
    return df

def simplify_label(label):
    label = str(label).lower()



    if "login" in label or "account" in label or "password" in label:
        return "Login Issue"
    elif "payment" in label or "billing" in label or "transaction" in label:
        return "Payment Issue"
    elif "refund" in label or "return" in label:
        return "Refund"
    elif "technical" in label or "bug" in label or "error" in label:
        return "Technical Issue"
    else:
        return "General Query"





def vectorize_text(texts):
    vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=6000,
    ngram_range=(1,2),
    min_df=3,
 
)
    X = vectorizer.fit_transform(texts)
    return X, vectorizer



if __name__ == "__main__":
    df = load_data()

    
    y = df["label"]   

    X = df["clean_text"]
    print(df["label"].value_counts())
    print("Samples:", len(df))
    print("Feature shape:", X.shape)
    print("Labels:", y.nunique(), "classes")