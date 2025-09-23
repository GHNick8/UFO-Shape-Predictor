import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api/predict"

st.set_page_config(page_title="UFO Shape Predictor", page_icon="🛸", layout="centered")

st.title("UFO Shape Prediction Dashboard")
st.write("Enter details about a UFO sighting and get a predicted shape from the ML model.")

# -------------------
# Input form
# -------------------
with st.form("ufo_form"):
    comments = st.text_area("Description of sighting", "Bright lights moving across the sky")
    duration_seconds = st.number_input("Duration (seconds)", min_value=0, value=60)
    country = st.text_input("Country code (e.g., us, ca, gb)", "us")
    year = st.number_input("Year", min_value=1900, max_value=2100, value=2023)
    month = st.number_input("Month", min_value=1, max_value=12, value=7)
    hour = st.number_input("Hour of day (0-23)", min_value=0, max_value=23, value=22)
    desc_length = len(comments)

    submitted = st.form_submit_button("Predict")

# -------------------
# Call API
# -------------------
if submitted:
    payload = {
        "comments": comments,
        "duration_seconds": duration_seconds,
        "country": country,
        "year": year,
        "month": month,
        "hour": hour,
        "desc_length": desc_length,
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Shape: **{result['predicted_shape']}**")
            st.metric(label="Confidence", value=f"{result['confidence']:.2f}")
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")