import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

random.seed(42)
np.random.seed(42)

NUM_DRIVERS = 10000

districts = [
    "Miraflores",
    "San Isidro",
    "Barranco",
    "La Molina",
    "Surco",
    "San Miguel",
    "Los Olivos",
    "Centro de Lima",
    "Ate",
    "Callao"
]

vehicle_types = [
    "Sedan",
    "SUV",
    "Motorbike",
    "Hatchback"
]

driver_statuses = [
    "Active",
    "Inactive"
]

drivers = []

for driver_id in range(1, NUM_DRIVERS + 1):

    age = random.randint(21, 65)

    experience_years = random.randint(1, 15)

    completed_rides = random.randint(50, 5000)

    driver_score = round(
        np.clip(
            np.random.normal(4.5, 0.4),
            2.5,
            5.0
        ),
        2
    )

    driver = {
        "driver_id": driver_id,
        "driver_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": age,
        "experience_years": experience_years,
        "driver_score": driver_score,
        "city": "Lima",
        "primary_zone": random.choice(districts),
        "vehicle_type": random.choice(vehicle_types),
        "completed_rides": completed_rides,
        "driver_status": random.choices(
            driver_statuses,
            weights=[0.92, 0.08]
        )[0],
        "join_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    }

    drivers.append(driver)

drivers_df = pd.DataFrame(drivers)

current_dir = os.path.dirname(__file__)

output_path = os.path.join(
    current_dir,
    "../../data/raw/drivers.csv"
)

drivers_df.to_csv(output_path, index=False)

print("drivers.csv generated successfully")