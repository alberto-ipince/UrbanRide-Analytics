import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

NUM_WEATHER_RECORDS = 5000

weather_conditions = [
    "Sunny",
    "Cloudy",
    "Foggy",
    "Rainy"
]

weather_data = []

start_date = datetime(2024, 1, 1)

for weather_id in range(1, NUM_WEATHER_RECORDS + 1):

    weather_condition = random.choices(
        weather_conditions,
        weights=[0.4, 0.35, 0.15, 0.10]
    )[0]

    if weather_condition == "Sunny":
        temperature = round(np.random.normal(28, 2), 1)
        rain_intensity = 0
        visibility = random.randint(8, 10)

    elif weather_condition == "Cloudy":
        temperature = round(np.random.normal(24, 2), 1)
        rain_intensity = random.randint(0, 1)
        visibility = random.randint(6, 9)

    elif weather_condition == "Foggy":
        temperature = round(np.random.normal(20, 2), 1)
        rain_intensity = 0
        visibility = random.randint(3, 6)

    else:
        temperature = round(np.random.normal(19, 2), 1)
        rain_intensity = random.randint(2, 10)
        visibility = random.randint(2, 5)

    weather_record = {
        "weather_id": weather_id,
        "record_datetime": start_date + timedelta(
            hours=random.randint(0, 8760)
        ),
        "weather_condition": weather_condition,
        "temperature_c": temperature,
        "rain_intensity": rain_intensity,
        "visibility_level": visibility
    }

    weather_data.append(weather_record)

weather_df = pd.DataFrame(weather_data)

current_dir = os.path.dirname(__file__)

output_path = os.path.join(
    current_dir,
    "../../data/raw/weather.csv"
)

weather_df.to_csv(output_path, index=False)

print("weather.csv generated successfully")