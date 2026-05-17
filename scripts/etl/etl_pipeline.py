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

# =========================
# FEATURE ENGINEERING
# =========================

print("\nCreating analytical features...")

# -------------------------
# DEMAND CATEGORY
# -------------------------

trips_df["demand_category"] = np.where(
    trips_df["demand_level"] >= 80,
    "High Demand",
    np.where(
        trips_df["demand_level"] >= 50,
        "Medium Demand",
        "Low Demand"
    )
)

# -------------------------
# SURGE IMPACT
# -------------------------

trips_df["surge_impact"] = (
    trips_df["final_fare"]
    - trips_df["base_fare"]
)

# -------------------------
# OPERATIONAL EFFICIENCY
# -------------------------

trips_df["operational_efficiency"] = round(
    trips_df["distance_km"]
    / trips_df["actual_duration_min"],
    2
)

# -------------------------
# PROFITABILITY SCORE
# -------------------------

trips_df["profitability_score"] = round(
    (
        trips_df["platform_revenue"]
        * trips_df["trip_satisfaction"]
    ) / 10,
    2
)

# -------------------------
# CUSTOMER EXPERIENCE SEGMENT
# -------------------------

trips_df["customer_experience_segment"] = np.where(
    trips_df["trip_satisfaction"] >= 4.5,
    "Excellent",
    np.where(
        trips_df["trip_satisfaction"] >= 3.5,
        "Good",
        np.where(
            trips_df["trip_satisfaction"] >= 2.5,
            "Average",
            "Poor"
        )
    )
)

print("Analytical features created")

# =========================
# EXPORT CLEANED DATASETS
# =========================

print("\nExporting cleaned datasets...")

trips_df.to_csv(
    os.path.join(CLEANED_PATH, "trips_cleaned.csv"),
    index=False
)

drivers_df.to_csv(
    os.path.join(CLEANED_PATH, "drivers_cleaned.csv"),
    index=False
)

customers_df.to_csv(
    os.path.join(CLEANED_PATH, "customers_cleaned.csv"),
    index=False
)

vehicles_df.to_csv(
    os.path.join(CLEANED_PATH, "vehicles_cleaned.csv"),
    index=False
)

zones_df.to_csv(
    os.path.join(CLEANED_PATH, "zones_cleaned.csv"),
    index=False
)

weather_df.to_csv(
    os.path.join(CLEANED_PATH, "weather_cleaned.csv"),
    index=False
)

payments_df.to_csv(
    os.path.join(CLEANED_PATH, "payments_cleaned.csv"),
    index=False
)

print("Cleaned datasets exported successfully")