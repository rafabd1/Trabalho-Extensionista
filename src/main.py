from fastapi import FastAPI
from pydantic import BaseModel
from .model import classify_text, load_artifacts

app = FastAPI(
    title="Phishing Detection API",
    description="An API to classify text as phishing or legitimate.",
    version="1.0.0"
)

# This will store the loaded model and vectorizer
model_artifacts = {}

@app.on_event("startup")
async def startup_event():
    """Load model artifacts on startup."""
    model_artifacts["vectorizer"], model_artifacts["model"] = load_artifacts()

class TextInput(BaseModel):
    text: str

@app.post("/classify/", summary="Classify a single text")
def classify(input: TextInput):
    """
    Receives a text and classifies it as phishing or legitimate.

    - **text**: The text to be classified.
    """
    vectorizer = model_artifacts["vectorizer"]
    model = model_artifacts["model"]
    print(f"Classifying text: {input.text}")
    return classify_text(input.text, vectorizer, model)