import pandas as pd
import random
import numpy as np
import os

random.seed(42)
np.random.seed(42)

NUM_VEHICLES = 12000

vehicle_types = {
    "Sedan": {
        "brands": ["Toyota", "Hyundai", "Kia", "Nissan"],
        "capacity": 4
    },
    "SUV": {
        "brands": ["Honda", "Mazda", "Ford", "Chevrolet"],
        "capacity": 6
    },
    "Motorbike": {
        "brands": ["Yamaha", "Honda", "Suzuki"],
        "capacity": 1
    },
    "Hatchback": {
        "brands": ["Kia", "Suzuki", "Volkswagen"],
        "capacity": 4
    }
}

fuel_types = [
    "Gasoline",
    "Hybrid",
    "Electric"
]

vehicle_statuses = [
    "Active",
    "Maintenance",
    "Inactive"
]

vehicles = []

for vehicle_id in range(1, NUM_VEHICLES + 1):

    vehicle_type = random.choice(
        list(vehicle_types.keys())
    )

    brand = random.choice(
        vehicle_types[vehicle_type]["brands"]
    )

    seating_capacity = vehicle_types[vehicle_type]["capacity"]

    model_year = random.randint(2012, 2026)

    fuel_type = random.choices(
        fuel_types,
        weights=[0.7, 0.2, 0.1]
    )[0]

    vehicle_status = random.choices(
        vehicle_statuses,
        weights=[0.9, 0.07, 0.03]
    )[0]

    vehicle = {
        "vehicle_id": vehicle_id,
        "vehicle_type": vehicle_type,
        "brand": brand,
        "model_year": model_year,
        "fuel_type": fuel_type,
        "seating_capacity": seating_capacity,
        "vehicle_status": vehicle_status
    }

    vehicles.append(vehicle)

vehicles_df = pd.DataFrame(vehicles)

current_dir = os.path.dirname(__file__)

output_path = os.path.join(
    current_dir,
    "../../data/raw/vehicles.csv"
)

vehicles_df.to_csv(output_path, index=False)

print("vehicles.csv generated successfully")