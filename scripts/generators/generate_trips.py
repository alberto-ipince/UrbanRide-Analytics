import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

NUM_TRIPS = 100000

# =========================
# LOAD DATASETS
# =========================

current_dir = os.path.dirname(__file__)

drivers_df = pd.read_csv(
    os.path.join(current_dir, "../../data/raw/drivers.csv")
)

customers_df = pd.read_csv(
    os.path.join(current_dir, "../../data/raw/customers.csv")
)

vehicles_df = pd.read_csv(
    os.path.join(current_dir, "../../data/raw/vehicles.csv")
)

zones_df = pd.read_csv(
    os.path.join(current_dir, "../../data/raw/zones.csv")
)

weather_df = pd.read_csv(
    os.path.join(current_dir, "../../data/raw/weather.csv")
)

payments_df = pd.read_csv(
    os.path.join(current_dir, "../../data/raw/payments.csv")
)

# =========================
# GENERATE TRIPS
# =========================

trips = []

start_date = datetime(2024, 1, 1)

for trip_id in range(1, NUM_TRIPS + 1):

    request_datetime = start_date + timedelta(
        minutes=random.randint(0, 525600)
    )

    pickup_delay = random.randint(2, 20)

    pickup_datetime = request_datetime + timedelta(
        minutes=pickup_delay
    )

    estimated_duration = random.randint(5, 90)

    dropoff_datetime = pickup_datetime + timedelta(
        minutes=estimated_duration
    )

    trip = {
        "trip_id": trip_id,

        "request_datetime": request_datetime,

        "pickup_datetime": pickup_datetime,

        "dropoff_datetime": dropoff_datetime,

        "customer_id": random.choice(
            customers_df["customer_id"].values
        ),

        "driver_id": random.choice(
            drivers_df["driver_id"].values
        ),

        "vehicle_id": random.choice(
            vehicles_df["vehicle_id"].values
        ),

        "zone_id": random.choice(
            zones_df["zone_id"].values
        ),

        "weather_id": random.choice(
            weather_df["weather_id"].values
        ),

        "payment_id": random.choice(
            payments_df["payment_id"].values
        )

        ,
        
        "is_peak_hour": (
            request_datetime.hour in [7, 8, 9, 18, 19, 20]
        ),

        "is_weekend": (
            request_datetime.weekday() >= 5
        ),

        "is_holiday": random.choices(
            [True, False],
            weights=[0.03, 0.97]
        )[0]
    }

    # =========================
    # TRAFFIC LEVEL
    # =========================

    if trip["is_peak_hour"]:
        traffic_level = random.choices(
            ["Medium", "High"],
            weights=[0.35, 0.65]
        )[0]
    else:
        traffic_level = random.choices(
            ["Low", "Medium", "High"],
            weights=[0.45, 0.45, 0.10]
        )[0]

    # =========================
    # DEMAND LEVEL
    # =========================

    if trip["is_peak_hour"] or trip["is_weekend"]:
        demand_level = random.randint(70, 100)
    else:
        demand_level = random.randint(30, 75)

    # =========================
    # ACTIVE REQUESTS
    # =========================

    active_requests = random.randint(
        demand_level * 2,
        demand_level * 5
    )

    # =========================
    # AVAILABLE DRIVERS
    # =========================

    available_drivers = random.randint(20, 500)

    # =========================
    # SAVE VARIABLES
    # =========================

    trip["traffic_level"] = traffic_level

    trip["demand_level"] = demand_level

    trip["active_requests"] = active_requests

    trip["available_drivers"] = available_drivers

        # =========================
    # DISTANCE
    # =========================

    distance_km = round(
        np.random.uniform(1.5, 25),
        2
    )

    # =========================
    # WAITING TIME
    # =========================

    if traffic_level == "High":
        waiting_time = random.randint(8, 20)
    elif traffic_level == "Medium":
        waiting_time = random.randint(4, 12)
    else:
        waiting_time = random.randint(2, 8)

    # =========================
    # ACTUAL DURATION
    # =========================

    if traffic_level == "High":
        actual_duration = estimated_duration + random.randint(10, 35)

    elif traffic_level == "Medium":
        actual_duration = estimated_duration + random.randint(5, 15)

    else:
        actual_duration = estimated_duration + random.randint(0, 8)

    # =========================
    # DYNAMIC PRICING
    # =========================

    surge_active = False

    dynamic_multiplier = 1.0

    if (
        demand_level >= 85
        and available_drivers <= 250
    ):

        surge_active = True

        dynamic_multiplier = round(
            np.random.uniform(1.2, 2.3),
            2
        )

    # =========================
    # FARES
    # =========================

    base_fare = round(
        4 + (distance_km * 2.2),
        2
    )

    final_fare = round(
        base_fare * dynamic_multiplier,
        2
    )

    # =========================
    # REVENUE SPLIT
    # =========================

    driver_earnings = round(
        final_fare * 0.75,
        2
    )

    platform_revenue = round(
        final_fare * 0.25,
        2
    )

    # =========================
    # SAVE FINANCIAL VARIABLES
    # =========================

    trip["distance_km"] = distance_km

    trip["waiting_time_min"] = waiting_time

    trip["estimated_duration_min"] = estimated_duration

    trip["actual_duration_min"] = actual_duration

    trip["surge_active"] = surge_active

    trip["dynamic_multiplier"] = dynamic_multiplier

    trip["base_fare"] = base_fare

    trip["final_fare"] = final_fare

    trip["driver_earnings"] = driver_earnings

    trip["platform_revenue"] = platform_revenue

        # =========================
    # RIDE STATUS
    # =========================

    ride_status = "Completed"

    cancellation_reason = None

    cancellation_probability = 0.03

    if traffic_level == "High":
        cancellation_probability += 0.05

    if surge_active:
        cancellation_probability += 0.04

    if waiting_time >= 15:
        cancellation_probability += 0.06

    cancelled = random.random() < cancellation_probability

    if cancelled:

        ride_status = "Cancelled"

        cancellation_reason = random.choice([
            "Driver unavailable",
            "Long wait time",
            "High fare",
            "Traffic congestion",
            "Customer cancelled"
        ])

    # =========================
    # CUSTOMER SATISFACTION
    # =========================

    satisfaction = 5.0

    satisfaction -= waiting_time * 0.05

    if traffic_level == "High":
        satisfaction -= 0.5

    if surge_active:
        satisfaction -= 0.4

    satisfaction = round(
        max(1, min(5, satisfaction)),
        2
    )

    # =========================
    # RATINGS
    # =========================

    customer_rating = round(
        np.clip(
            np.random.normal(satisfaction, 0.4),
            1,
            5
        ),
        2
    )

    driver_rating = round(
        np.clip(
            np.random.normal(4.5, 0.3),
            1,
            5
        ),
        2
    )

    # =========================
    # COMPLAINTS
    # =========================

    complaint_registered = random.random() < 0.08

    if satisfaction <= 2.5:
        complaint_registered = random.random() < 0.45

    # =========================
    # SAVE EXPERIENCE VARIABLES
    # =========================

    trip["ride_status"] = ride_status

    trip["cancellation_reason"] = cancellation_reason

    trip["trip_satisfaction"] = satisfaction

    trip["customer_rating"] = customer_rating

    trip["driver_rating"] = driver_rating

    trip["complaint_registered"] = complaint_registered

    trips.append(trip)

trips_df = pd.DataFrame(trips)

# =========================
# CONTROLLED DATA ISSUES
# =========================

# RANDOM NULLS

trips_df["complaint_registered"] = (
    trips_df["complaint_registered"].astype("object")
)

null_sample_1 = trips_df.sample(
    frac=0.02,
    random_state=42
).index

trips_df.loc[
    null_sample_1,
    "customer_rating"
] = np.nan

null_sample_2 = trips_df.sample(
    frac=0.01,
    random_state=24
).index

trips_df.loc[
    null_sample_2,
    "complaint_registered"
] = np.nan

# TYPO INCONSISTENCIES

zone_typo_sample = trips_df.sample(
    frac=0.005,
    random_state=15
).index

trips_df.loc[
    zone_typo_sample,
    "traffic_level"
] = "Hgh"

# OUTLIERS

outlier_sample = trips_df.sample(
    frac=0.003,
    random_state=77
).index

trips_df.loc[
    outlier_sample,
    "actual_duration_min"
] *= 3

# DUPLICATES

duplicate_rows = trips_df.sample(
    frac=0.002,
    random_state=99
)

trips_df = pd.concat(
    [trips_df, duplicate_rows],
    ignore_index=True
)

# =========================
# EXPORT CSV
# =========================

output_path = os.path.join(
    current_dir,
    "../../data/raw/trips.csv"
)

trips_df.to_csv(output_path, index=False)

print("trips.csv generated successfully")