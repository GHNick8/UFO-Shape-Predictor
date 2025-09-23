import os
import logging
import argparse
from pathlib import Path
import pandas as pd
import yaml

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

def load_config(config_path: str):
    """Load config.yaml file"""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
    
def clean_ufo_data(input_path: str, output_path: str):
    """Read raw UFO CSV, clean it, and save to processed folder."""
    logging.info(f"Loading data from {input_path}...")
    df = pd.read_csv(input_path)

    # Convert datetime
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

    # Clean text fields
    for col in ["city", "state", "country", "shape"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()

    #Convert duration to numeric
    if "duration (seconds)" in df.columns:
        df["duration (seconds)"] = pd.to_numeric(
            df["duration (seconds)"], errors="coerce"
        )

    # Drop rows missing essential values 
    essential_cols = ["datetime", "city", "country", "comments"]
    df = df.dropna(subset=[c for c in essential_cols if c in df.columns])

    logging.info(f"Saving cleaned data to {output_path}...")
    df.to_csv(output_path, index=False)
    logging.info("Clean data saved successfully.")

def main(config_path: str):
    config = load_config(config_path)

    raw_data = Path(config["data"]["raw"]) / "ufo.csv"
    processed_data = Path(config["data"]["processed"]) / "clean_ufo.csv"

    clean_ufo_data(raw_data, processed_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean UFO dataset")
    parser.add_argument("--config", default="config/config.yaml", help="Path to config file")
    args = parser.parse_args()
    main(args.config)