import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime

# Define constants
store_locations = [
    "Madison Avenue",
    "Soho",
    "Westfield World Trade Center",
    "Rodeo Drive",
    "South Coast Plaza",
    "San Francisco Centre",
    "Bal Harbour Shops",
    "Aventura Mall",
    "NorthPark Center",
    "The Galleria",
    "Oak Street",
    "Yorkdale Shopping Centre",
    "Pacific Centre",
    "El Palacio de Hierro (Polanco)",
    "El Palacio de Hierro (Santa Fe)",
]

handbag_types = [
    "Ella Tote",
    "Perry Tote",
    "Gemini Link Tote",
    "Kira Chevron Tote",
    "T Monogram Tote",
    "Robinson Tote",
    "McGraw Tote",
    "Britten Tote",
]

colors = [
    "Multi",
    "Black",
    "Blue",
    "Brown",
    "Gray",
    "Green",
    "Pink",
    "Purple",
    "Red",
    "White",
    "Yellow",
    "Beige",
    "Metallic",
]
materials = ["Canvas", "Leather", "Jacquard", "Pebbled Leather", "Coated Canvas"]
bag_sizes = ["Mini", "Small", "Medium", "Large"]

# Manufacturing and shipping considerations
#
manufacturing_cities = ["Guangzhou", "Shenzhen", "Ho Chi Minh City", "Hanoi", "Da Nang"]
lead_time_range = (30, 50)  # Lead time range in days
shipping_time_range = (14, 18)  # Shipping time range in days

# Seasonal demand multipliers (arbitrary example)
seasonal_demand = {"Winter": 0.8, "Spring": 1.2, "Summer": 1.0, "Fall": 1.1}


# Generate synthetic data
def generate_dataset(n_samples=1000):
    data = []
    today = datetime.today()

    for _ in range(n_samples):
        store = random.choice(store_locations)
        handbag = random.choice(handbag_types)
        color = random.choice(colors)
        material = random.choice(materials)
        size = random.choice(bag_sizes)

        manufacturing_cities = random.choice(manufacturing_cities)
        lead_time = random.randint(*lead_time_range)
        shipping_time = random.randint(*shipping_time_range)
        total_lead_time = lead_time + shipping_time

        season = random.choice(list(seasonal_demand.keys()))
        demand_multiplier = seasonal_demand[season]

        # Simulate demand and stock
        base_demand = random.randint(50, 300)  # Base demand per store per season
        adjusted_demand = int(base_demand * demand_multiplier)
        stock_level = random.randint(
            0, adjusted_demand + 50
        )  # Simulate potential overfill/underfill

        data.append(
            {
                "Store": store,
                "Handbag Type": handbag,
                "Color": color,
                "Material": material,
                "Size": size,
                "Manufacturing City": manufacturing_cities,
                "Lead Time (Days)": lead_time,
                "Shipping Time (Days)": shipping_time,
                "Total Lead Time (Days)": total_lead_time,
                "Season": season,
                "Base Demand": base_demand,
                "Adjusted Demand": adjusted_demand,
                "Stock Level": stock_level,
                "Overfill/Underfill": stock_level - adjusted_demand,
            }
        )

    return pd.DataFrame(data)


# Generate and save the dataset
dataset = generate_dataset(2000)  # Generate 2000 samples
dataset.to_csv("tory_burch_inventory_dataset.csv", index=False)

print("Synthetic dataset created and saved as 'tory_burch_inventory_dataset.csv'.")
