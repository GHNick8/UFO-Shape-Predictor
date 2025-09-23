🛸 UFO Shape Predictor

An end-to-end MLOps project that predicts the most likely UFO shape from user-submitted sighting details. Built with XGBoost, FastAPI, and a modern HTML/Streamlit frontend.

✨ Features

🔄 Data Pipeline: cleans raw UFO sightings dataset, extracts features (text length, time, location).

🤖 Model Training: XGBoost classifier trained to predict UFO shapes.

🏷️ Label Encoding: converts UFO shape labels into numeric classes for training.

⚡ API Service: FastAPI backend with both HTML form and JSON API.

🖥️ Dashboards:

HTML frontend (modern grey UI, styled with CSS).

Streamlit dashboard for interactive exploration.

🎨 Custom UI: styled dark/grey theme, with a neon green accent and a UFO favicon.

✅ Testing: basic API tests with pytest.

📂 Project Structure
ufo-mlops-project/
│
├── src/ufo_mlops/
│   ├── models/
│   │   ├── train.py          # Train XGBoost model
│   │   ├── predict.py        # Local prediction script
│   ├── data/                 # Data pipeline code
│   └── ...
│
├── api/
│   └── main.py               # FastAPI app (HTML + JSON API)
│
├── dashboards/
│   └── app.py                # Streamlit dashboard
│
├── templates/
│   └── index.html            # HTML frontend
│
├── static/
│   ├── style.css             # Modern grey UI styles
│   └── favicon.ico           # UFO favicon
│
├── models/
│   ├── ufo_model.pkl         # Trained XGBoost model
│   └── label_encoder.pkl     # Label encoder for UFO shapes
│
├── requirements.txt
└── README.md

⚙️ Setup
1. Clone repo & install dependencies
git clone https://github.com/yourname/ufo-mlops-project.git
cd ufo-mlops-project
pip install -r requirements.txt

2. Train the model
python src/ufo_mlops/models/train.py --config config/config.yaml


This creates:

models/ufo_model.pkl

models/label_encoder.pkl

3. Run FastAPI backend
uvicorn api.main:app --reload


App runs at: http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs

4. Run Streamlit dashboard (optional)
streamlit run dashboards/app.py


Runs at: http://localhost:8501

🎨 UI Preview

Modern grey/dark theme with neon green accent.

Centered form + prediction box with consistent width.

Custom UFO favicon in browser tab.

🚀 Deployment

Works locally with FastAPI + Streamlit.

Can be imported into Replit (FastAPI recommended).

Docker/Compose setup possible for cloud deployment.

📊 Example Prediction

Input:

{
  "comments": "Bright lights hovering silently in the night sky",
  "duration_seconds": 120,
  "country": "us",
  "year": 2022,
  "month": 7,
  "hour": 22,
  "desc_length": 42
}


Output:

{
  "predicted_shape": "light",
  "confidence": 0.81
}

🛠️ Tech Stack

Python 3.10+

FastAPI + Jinja2 templates

Streamlit

scikit-learn, XGBoost, pandas

Joblib for model persistence

pytest for testing

🚧 Future Improvements

Hyperparameter tuning (GridSearch / Optuna).

Experiment tracking with MLflow/DVC.

CI/CD with GitHub Actions.

Deployment to cloud (Render, Railway, or Docker Compose).

👽 About

This project is part of my MLOps learning journey.
It combines data science, production deployment, and frontend styling into a complete end-to-end ML application.