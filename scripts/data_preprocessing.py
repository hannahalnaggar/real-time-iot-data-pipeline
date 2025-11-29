""""Role 2: Data Quality & Preprocessing
- Created preprocessing script
- Cleaned dummy IoT data (data/cleaned_data.csv)
- Ready to process real data once Task 1 completes"""


import pandas as pd
import os

RAW_FILE = "data/data_log.csv"
OUT_FILE = "data/cleaned_data.csv"

def load_raw():
    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError(f"{RAW_FILE} not found. Create dummy data first.")
    return pd.read_csv(RAW_FILE)

def clean_data(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")

    # Drop missing essential info
    df = df.dropna(subset=["timestamp", "sensor_id", "temperature", "humidity"])

    # Remove duplicates
    df = df.drop_duplicates(subset=["timestamp", "sensor_id"])

    # Filter valid ranges
    df = df[(df["temperature"] >= -40) & (df["temperature"] <= 100)]
    df = df[(df["humidity"] >= 0) & (df["humidity"] <= 100)]
    return df

def add_features(df):
    df["temp_status"] = df["temperature"].apply(
        lambda x: "Critical" if x > 45 else "High" if x > 35 else "Normal"
    )
    df["humidity_status"] = df["humidity"].apply(
        lambda x: "Dry" if x < 30 else "Normal" if x <= 60 else "Wet"
    )
    df["anomaly_flag"] = df.apply(
        lambda row: 1 if (row.temperature > 50 or row.humidity > 90) else 0,
        axis=1
    )
    return df

def save_output(df):
    df.to_csv(OUT_FILE, index=False)
    print(f"Cleaned data saved to {OUT_FILE}. Rows: {len(df)}")

if __name__ == "__main__":
    raw = load_raw()
    cleaned = clean_data(raw)
    final = add_features(cleaned)
    save_output(final)
