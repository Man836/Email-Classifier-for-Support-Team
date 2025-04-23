# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

def train_model(data_path="data/combined_emails_with_natural_pii.csv"):
    df = pd.read_csv(data_path)
    X = df["email_text"]
    y = df["category"]

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    model.fit(X, y)
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/classifier.pkl")
