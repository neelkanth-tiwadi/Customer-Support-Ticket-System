from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer():
    return TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_features=3000
    )