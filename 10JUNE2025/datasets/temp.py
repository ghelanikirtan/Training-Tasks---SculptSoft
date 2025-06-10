import pandas as pd
import numpy as np

# Define Indian batters with real stats (ODI-inspired from ESPNcricinfo)
batters = [
    {"id": 1, "name": "Virat Kohli", "average": 58.0, "strike_rate": 93.0, "bonus_condition": lambda t, w, p, o: p == "dry"},
    {"id": 2, "name": "Rohit Sharma", "average": 49.0, "strike_rate": 90.0, "bonus_condition": lambda t, w, p, o: p == "green"},
    {"id": 3, "name": "Shubman Gill", "average": 57.0, "strike_rate": 102.0, "bonus_condition": lambda t, w, p, o: o > 7},
    {"id": 4, "name": "Yashasvi Jaiswal", "average": 45.0, "strike_rate": 105.0, "bonus_condition": lambda t, w, p, o: w > 15},
    {"id": 5, "name": "KL Rahul", "average": 50.0, "strike_rate": 87.0, "bonus_condition": lambda t, w, p, o: False}
]

# Generate balanced dataset
n_rows = 5000
rows_per_batter = n_rows // len(batters) 
data = {
    "temperature": [],
    "wind_speed": [],
    "pitch_condition": [],
    "opposition_strength": [],
    "best_batter": []
}

for batter in batters:
    batter_id = batter["id"]
    for _ in range(rows_per_batter):
        # Generate conditions favoring the batter's strength
        if batter_id == 1:  # Kohli: dry pitch
            pitch = "dry"
            t = np.random.uniform(15, 40)
            w = np.random.uniform(0, 30)
            o = np.random.randint(1, 11)
        elif batter_id == 2:  # Rohit: green pitch
            pitch = "green"
            t = np.random.uniform(15, 40)
            w = np.random.uniform(0, 30)
            o = np.random.randint(1, 11)
        elif batter_id == 3:  # Gill: strong opposition
            pitch = np.random.choice(["green", "dry", "hard", "dusty"])
            t = np.random.uniform(15, 40)
            w = np.random.uniform(0, 30)
            o = np.random.randint(8, 11)  # Ensure o > 7
        elif batter_id == 4:  # Jaiswal: windy
            pitch = np.random.choice(["green", "dry", "hard", "dusty"])
            t = np.random.uniform(15, 40)
            w = np.random.uniform(15.1, 30)  # Ensure w > 15
            o = np.random.randint(1, 11)
        else:  # Rahul: no specific condition
            pitch = np.random.choice(["green", "dry", "hard", "dusty"])
            t = np.random.uniform(15, 40)
            w = np.random.uniform(0, 30)
            o = np.random.randint(1, 11)
        
        data["temperature"].append(t)
        data["wind_speed"].append(w)
        data["pitch_condition"].append(pitch)
        data["opposition_strength"].append(o)
        data["best_batter"].append(batter_id)

# Create DataFrame
df = pd.DataFrame(data)

# One-hot encode pitch_condition
pitch_dummies = pd.get_dummies(df["pitch_condition"], prefix="pitch")
df = pd.concat([df, pitch_dummies], axis=1)
df = df.drop("pitch_condition", axis=1)

# Save to CSV
df.to_csv("./datasets/cricket_knn_indian_players_balanced.csv", index=False)
print("Balanced dataset saved as 'cricket_knn_indian_players_balanced.csv' with 500 rows.")