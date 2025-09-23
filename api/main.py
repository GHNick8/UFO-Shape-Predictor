from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pathlib
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# -------------------
# Load model
# -------------------
MODEL_PATH = pathlib.Path("models/ufo_model.pkl")

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

logging.info(f"Loading model from {MODEL_PATH}...")
model = joblib.load(MODEL_PATH)

# -------------------
# FastAPI app
# -------------------
app = FastAPI(title="UFO Shape Prediction API")

# -------------------
# Request Schema
# -------------------
class Sighting(BaseModel):
    comments: str
    duration_seconds: float
    country: str
    year: int
    month: int
    hour: int
    desc_length: int

# -------------------
# Routes
# -------------------
@app.get("/")
def root():
    return {"message": "Welcome to the UFO Prediction API! Use /docs to try it out."}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "UFO API is running!"}

@app.post("/predict")
def predict(sighting: Sighting):
    # Convert input to DataFrame
    data = pd.DataFrame([{
        "comments": sighting.comments,
        "duration (seconds)": sighting.duration_seconds,
        "country": sighting.country,
        "year": sighting.year,
        "month": sighting.month,
        "hour": sighting.hour,
        "desc_length": sighting.desc_length
    }])

    # Predict
    prediction = model.predict(data)[0]
    confidence = model.predict_proba(data).max()

    return {
        "predicted_shape": prediction,
        "confidence": round(float(confidence), 2)
    }
