import logging
import argparse
import pandas as pd
from pathlib import Path
import yaml

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

def load_schema(schema_path: str):
    with open(schema_path, "r") as f:
        return yaml.safe_load(f)
    
def validate_schema(df: pd.DataFrame, schema: dict):
    """Check dataframe matches expected schema."""
    for col, dtype in schema["columns"].items():
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
        if dtype == "datetime64[ns]":
            if not pd.api.types.is_datetime64_any_dtype(df[col]):
                raise TypeError(f"Column {col} must be datetime")
        elif dtype == "str":
            if df[col].dtype != "object":
                raise TypeError(f"Column {col} must be string")
        elif dtype == "float":
            if not pd.api.types.is_float_dtype(df[col]):
                raise TypeError(f"Column {col} must be float")

def build_features(input_path: str, output_path: str, schema_path: str):
    logging.info(f"Loading processed data from {input_path}...")
    df = pd.read_csv(input_path, parse_dates=["datetime"])

    # Vaildate schema
    schema = load_schema(schema_path)
    validate_schema(df, schema)

    logging.info("Schema validation passed")

    # Feature engineering
    df["year"] = df["datetime"].dt.year
    df["month"] = df["datetime"].dt.month
    df["hour"] = df["datetime"].dt.hour

    # Example text feature: Length of description
    df["desc_length"] = df["comments"].astype(str).apply(len)

    # Save features dataset
    df.to_csv(output_path, index=False)
    logging.info(f"Features saved to {output_path}")

def main(config_path: str, schema_path: str):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    processed_data = Path(config["data"]["processed"]) / "clean_ufo.csv"
    feature_data = Path(config["data"]["processed"]) / "features_ufo.csv"

    build_features(processed_data, feature_data, schema_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build features for UFO dataset")
    parser.add_argument("--config", default="config/config.yaml", help="Path to config file")
    parser.add_argument("--schema", default="schema.yaml", help="Path to schema file")
    args = parser.parse_args()
    main(args.config, args.schema)