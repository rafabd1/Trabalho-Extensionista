import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

artifacts_dir = "artifacts"
vectorizer_path = os.path.join(artifacts_dir, "vectorizer.joblib")
model_path = os.path.join(artifacts_dir, "model.joblib")

def load_artifacts():
    """Loads the saved model and vectorizer."""
    if not (os.path.exists(vectorizer_path) and os.path.exists(model_path)):
        raise RuntimeError(f"Model artifacts not found in '{os.path.abspath(artifacts_dir)}'. Please run 'python src/train.py' first.")

    print("Loading model artifacts...")
    vectorizer = joblib.load(vectorizer_path)
    model = joblib.load(model_path)
    print("Model artifacts loaded successfully.")
    return vectorizer, model

def classify_text(text_to_classify: str, vectorizer: TfidfVectorizer, model: LogisticRegression):
    """
    Classify a text as phishing (1) or legitimate (0)
    """
    text_features = vectorizer.transform([text_to_classify])
    prediction = model.predict(text_features)[0]
    probability = model.predict_proba(text_features)[0]
    
    result = {
        'is_phishing': bool(prediction),
        'confidence': float(probability[1] if prediction == 1 else probability[0])
    }
    return result 