import pandas as pd
import os

zones = [
    {
        "zone_id": 1,
        "district": "Miraflores",
        "zone_type": "Commercial",
        "latitude": -12.1211,
        "longitude": -77.0297,
        "avg_traffic_score": 85,
        "avg_demand_score": 90
    },
    {
        "zone_id": 2,
        "district": "San Isidro",
        "zone_type": "Business",
        "latitude": -12.0975,
        "longitude": -77.0365,
        "avg_traffic_score": 88,
        "avg_demand_score": 92
    },
    {
        "zone_id": 3,
        "district": "Barranco",
        "zone_type": "Tourist",
        "latitude": -12.1465,
        "longitude": -77.0209,
        "avg_traffic_score": 70,
        "avg_demand_score": 80
    },
    {
        "zone_id": 4,
        "district": "La Molina",
        "zone_type": "Residential",
        "latitude": -12.0878,
        "longitude": -76.9527,
        "avg_traffic_score": 65,
        "avg_demand_score": 72
    },
    {
        "zone_id": 5,
        "district": "Surco",
        "zone_type": "Residential",
        "latitude": -12.1450,
        "longitude": -76.9910,
        "avg_traffic_score": 75,
        "avg_demand_score": 78
    },
    {
        "zone_id": 6,
        "district": "San Miguel",
        "zone_type": "Residential",
        "latitude": -12.0780,
        "longitude": -77.0830,
        "avg_traffic_score": 68,
        "avg_demand_score": 70
    },
    {
        "zone_id": 7,
        "district": "Los Olivos",
        "zone_type": "Residential",
        "latitude": -11.9910,
        "longitude": -77.0700,
        "avg_traffic_score": 72,
        "avg_demand_score": 76
    },
    {
        "zone_id": 8,
        "district": "Centro de Lima",
        "zone_type": "Commercial",
        "latitude": -12.0464,
        "longitude": -77.0428,
        "avg_traffic_score": 95,
        "avg_demand_score": 93
    },
    {
        "zone_id": 9,
        "district": "Ate",
        "zone_type": "Residential",
        "latitude": -12.0432,
        "longitude": -76.9426,
        "avg_traffic_score": 74,
        "avg_demand_score": 73
    },
    {
        "zone_id": 10,
        "district": "Callao",
        "zone_type": "Logistics",
        "latitude": -12.0500,
        "longitude": -77.1250,
        "avg_traffic_score": 82,
        "avg_demand_score": 77
    }
]

zones_df = pd.DataFrame(zones)

current_dir = os.path.dirname(__file__)

output_path = os.path.join(
    current_dir,
    "../../data/raw/zones.csv"
)

zones_df.to_csv(output_path, index=False)

print("zones.csv generated successfully")