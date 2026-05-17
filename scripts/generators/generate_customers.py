import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 40000

customer_segments = [
    "Regular",
    "Premium",
    "Business"
]

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

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    segment = random.choices(
        customer_segments,
        weights=[0.7, 0.2, 0.1]
    )[0]

    if segment == "Business":
        total_rides = random.randint(80, 1500)
        avg_rating = round(
            np.clip(np.random.normal(4.7, 0.2), 3.5, 5.0),
            2
        )

    elif segment == "Premium":
        total_rides = random.randint(40, 900)
        avg_rating = round(
            np.clip(np.random.normal(4.6, 0.3), 3.0, 5.0),
            2
        )

    else:
        total_rides = random.randint(1, 400)
        avg_rating = round(
            np.clip(np.random.normal(4.3, 0.5), 2.5, 5.0),
            2
        )

    repeat_customer = total_rides >= 50

    customer = {
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 65),
        "customer_segment": segment,
        "registration_date": fake.date_between(
            start_date="-6y",
            end_date="today"
        ),
        "total_rides": total_rides,
        "average_rating_given": avg_rating,
        "repeat_customer": repeat_customer,
        "city": "Lima",
        "district": random.choice(districts)
    }

    customers.append(customer)

customers_df = pd.DataFrame(customers)

current_dir = os.path.dirname(__file__)

output_path = os.path.join(
    current_dir,
    "../../data/raw/customers.csv"
)

customers_df.to_csv(output_path, index=False)

print("customers.csv generated successfully")