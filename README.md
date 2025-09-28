# UFO Shape Predictor (Replit Edition)

Predict UFO shapes from sighting details with a trained ML model.
Built with FastAPI, XGBoost, and a modern dark/grey HTML frontend.

## Try it on Replit

Click Run ▶️ in Replit.

Wait until the server starts (uvicorn running on 0.0.0.0:8000).

Open the Webview or the public Replit link.

You’ll see a form like this:

📝 Enter description of the sighting

⏱ Duration in seconds

🌍 Country code (us, ca, gb…)

📅 Year, Month

⏰ Hour of day

Click Predict → the app will return the most likely UFO shape and a confidence score.

## Files in this Replit

api/main.py → FastAPI app

templates/index.html → HTML UI

static/style.css → Styling (modern grey theme)

static/favicon.ico → UFO favicon

models/ufo_model.pkl → Trained XGBoost model

models/label_encoder.pkl → Label encoder for UFO shapes

requirements.txt → Python dependencies

## How it Works

FastAPI serves an HTML form at /

Model + encoder are loaded from models/

User input is converted into features

XGBoost model predicts UFO shape → decoded into a string

Result displayed directly in the web app

## Requirements

Already in requirements.txt:

fastapi
uvicorn
pandas
scikit-learn
xgboost
joblib
jinja2


Replit installs these automatically.

## Example

Input:

Comments: “Bright lights hovering silently”

Duration: 120

Country: us

Year: 2023

Month: 7

Hour: 22

## About

This project is part of an MLOps learning journey — data science meets deployment, now running fully online on Replit 🚀
