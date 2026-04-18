import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


from .vectorizer import create_vectorizer
from .data_preprocessing import load_data


def train():
    df = load_data()

    X = df["clean_text"]
    y = df["label"]

    vectorizer = create_vectorizer()
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42
    )

    model = MultinomialNB() 
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print("Accuracy:", round(acc, 3))

    pickle.dump(model, open("src/models/model.pkl", "wb"))
    pickle.dump(vectorizer, open("src/models/vectorizer.pkl", "wb"))


if __name__ == "__main__":
    train()