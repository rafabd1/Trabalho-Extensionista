import joblib
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import os

artifacts_dir = "artifacts"
os.makedirs(artifacts_dir, exist_ok=True)

print("Loading dataset...")
dataset_reduced = load_dataset("ealvaradob/phishing-dataset", "combined_reduced", trust_remote_code=True)

df = dataset_reduced['train'].to_pandas()

text = df['text'].values
labels = df['label'].values

train_text, _, train_labels, _ = train_test_split(
    text, labels, test_size=0.2, random_state=42
)

print("Training vectorizer...")
vectorizer = TfidfVectorizer(max_features=5000)
vectorizer.fit(train_text)

print("Transforming text...")
train_features = vectorizer.transform(train_text)

print("Training model...")
model = LogisticRegression(max_iter=1000)
model.fit(train_features, train_labels)

print("Saving artifacts...")
joblib.dump(vectorizer, os.path.join(artifacts_dir, "vectorizer.joblib"))
joblib.dump(model, os.path.join(artifacts_dir, "model.joblib"))

print("Training complete and artifacts saved.") 