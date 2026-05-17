import pandas as pd
import numpy as np
import os

# =========================
# PATHS
# =========================

BASE_DIR = os.path.dirname(__file__)

RAW_PATH = os.path.join(
    BASE_DIR,
    "../../data/raw"
)

CLEANED_PATH = os.path.join(
    BASE_DIR,
    "../../data/cleaned"
)

# =========================
# LOAD DATASETS
# =========================

trips_df = pd.read_csv(
    os.path.join(RAW_PATH, "trips.csv")
)

drivers_df = pd.read_csv(
    os.path.join(RAW_PATH, "drivers.csv")
)

customers_df = pd.read_csv(
    os.path.join(RAW_PATH, "customers.csv")
)

vehicles_df = pd.read_csv(
    os.path.join(RAW_PATH, "vehicles.csv")
)

zones_df = pd.read_csv(
    os.path.join(RAW_PATH, "zones.csv")
)

weather_df = pd.read_csv(
    os.path.join(RAW_PATH, "weather.csv")
)

payments_df = pd.read_csv(
    os.path.join(RAW_PATH, "payments.csv")
)

print("Datasets loaded successfully")

# =========================
# TRIPS CLEANING
# =========================

print("\nCleaning trips dataset...")

# -------------------------
# REMOVE DUPLICATES
# -------------------------

initial_rows = len(trips_df)

trips_df = trips_df.drop_duplicates()

duplicates_removed = initial_rows - len(trips_df)

print(f"Duplicates removed: {duplicates_removed}")

# -------------------------
# FIX TYPO INCONSISTENCIES
# -------------------------

trips_df["traffic_level"] = (
    trips_df["traffic_level"]
    .replace({
        "Hgh": "High"
    })
)

print("Traffic level typos fixed")

# -------------------------
# HANDLE NULLS
# -------------------------

trips_df["customer_rating"] = (
    trips_df["customer_rating"]
    .fillna(
        trips_df["customer_rating"].median()
    )
)

trips_df["complaint_registered"] = (
    trips_df["complaint_registered"]
    .fillna(False)
)

print("Null values handled")

# -------------------------
# HANDLE OUTLIERS
# -------------------------

duration_cap = (
    trips_df["actual_duration_min"]
    .quantile(0.99)
)

trips_df["actual_duration_min"] = np.where(
    trips_df["actual_duration_min"] > duration_cap,
    duration_cap,
    trips_df["actual_duration_min"]
)

print("Outliers capped")

# -------------------------
# DATA TYPE NORMALIZATION
# -------------------------

trips_df["request_datetime"] = pd.to_datetime(
    trips_df["request_datetime"]
)

trips_df["pickup_datetime"] = pd.to_datetime(
    trips_df["pickup_datetime"]
)

trips_df["dropoff_datetime"] = pd.to_datetime(
    trips_df["dropoff_datetime"]
)

print("Datetime conversion completed")