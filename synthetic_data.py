import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)  # For reproducibility

# Configuration
num_days = 90
start_date = datetime(2025, 2, 1)
stores = ["New York", "Los Angeles"]
dress_categories = {"New York": "Black Short Dress", "Los Angeles": "Casual Day Dress"}

price_ranges = {"Black Short Dress": (300, 400), "Casual Day Dress": (200, 350)}

rows = []
record_id = 1

for store in stores:
    # Use one category per store, or you can add more categories for variety
    category = dress_categories[store]
    price_low, price_high = price_ranges[category]

    for day_offset in range(num_days):
        date = start_date + timedelta(days=day_offset)

        # Historical demand: let's use a random normal distribution
        if category == "Black Short Dress":
            historical_demand = int(np.random.normal(20, 5))  # mean=20, std=5
        else:
            historical_demand = int(np.random.normal(15, 3))  # mean=15, std=3

        # Make sure historical demand is not negative
        historical_demand = max(historical_demand, 0)

        # Inventory on-hand: random integer
        inventory_on_hand = np.random.randint(0, 100)  # 0-99 units in stock

        # Price
        price = round(np.random.uniform(price_low, price_high), 2)

        # Lead time
        lead_time = np.random.randint(5, 15)  # 5-14 days

        # Forecast demand: slightly correlated with historical demand
        # Let's say forecast is historical_demand * (1 +/- 20% random factor)
        forecast_multiplier = 1 + np.random.uniform(-0.2, 0.2)
        forecast_demand = int(historical_demand * forecast_multiplier)

        # Overfill / Underfill logic
        # If (inventory_on_hand - forecast_demand) > some threshold => Overfill
        # If (inventory_on_hand - forecast_demand) < some threshold => Underfill
        # We'll keep it simple and say if difference > 10 => Overfill, < -10 => Underfill
        diff = inventory_on_hand - forecast_demand
        if diff > 10:
            flag = "Overfill"
        elif diff < -10:
            flag = "Underfill"
        else:
            flag = "Balanced"

        row = {
            "Record_ID": record_id,
            "Date": date.strftime("%Y-%m-%d"),
            "Store": store,
            "Dress_Category": category,
            "Price": price,
            "Historical_Demand": historical_demand,
            "Inventory_On_Hand": inventory_on_hand,
            "Lead_Time_Days": lead_time,
            "Forecast_Demand": forecast_demand,
            "Overfill_Underfill_Flag": flag,
        }
        rows.append(row)
        record_id += 1

# Create DataFrame
df = pd.DataFrame(rows)
print(df.head(10))

# Save to CSV (e.g., local) — then you can upload the CSV to S3
df.to_csv("synthetic_inventory_data.csv", index=False)
