from fastapi import FastAPI, Request, Form, Body
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import pathlib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# -------------------
# Load model + encoder
# -------------------
MODEL_PATH = pathlib.Path("models/ufo_model.pkl")
ENCODER_PATH = pathlib.Path("models/label_encoder.pkl")

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
if not ENCODER_PATH.exists():
    raise FileNotFoundError(f"Label encoder not found at {ENCODER_PATH}")

logging.info(f"Loading model from {MODEL_PATH}...")
model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)

# -------------------
# FastAPI app
# -------------------
app = FastAPI(title="UFO Shape Prediction API + HTML")

# Mount static + templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# -------------------
# HTML routes
# -------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    comments: str = Form(...),
    duration_seconds: int = Form(...),
    country: str = Form(...),
    year: int = Form(...),
    month: int = Form(...),
    hour: int = Form(...)
):
    desc_length = len(comments)

    data = pd.DataFrame([{
        "comments": comments,
        "duration (seconds)": duration_seconds,
        "country": country,
        "year": year,
        "month": month,
        "hour": hour,
        "desc_length": desc_length
    }])

    # Predict numeric class
    prediction_idx = model.predict(data)[0]
    confidence = model.predict_proba(data).max()

    # Decode to UFO shape string
    prediction_label = label_encoder.inverse_transform([prediction_idx])[0]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "predicted_shape": prediction_label,
            "confidence": round(float(confidence), 2)
        }
    )

@app.post("/api/predict")
def api_predict(payload: dict = Body(...)):
    # Rename keys to match training features
    payload_renamed = {
        "comments": payload.get("comments", ""),
        "duration (seconds)": payload.get("duration_seconds", 0),
        "country": payload.get("country", "unknown"),
        "year": payload.get("year", 0),
        "month": payload.get("month", 0),
        "hour": payload.get("hour", 0),
        "desc_length": payload.get("desc_length", 0),
    }

    data = pd.DataFrame([payload_renamed])

    # Predict numeric class
    prediction_idx = model.predict(data)[0]
    confidence = model.predict_proba(data).max()

    # Decode label
    prediction_label = label_encoder.inverse_transform([prediction_idx])[0]

    return {
        "predicted_shape": prediction_label,
        "confidence": round(float(confidence), 2)
    }
