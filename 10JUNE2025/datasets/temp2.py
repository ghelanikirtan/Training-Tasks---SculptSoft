import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Define Indian batters with real stats (ODI-inspired from ESPNcricinfo)
batters = [
    {"id": 1, "name": "Virat Kohli", "average": 58.0, "strike_rate": 93.0, "bonus_condition": lambda h, w, p, o: p == "dry"},
    {"id": 2, "name": "Rohit Sharma", "average": 49.0, "strike_rate": 90.0, "bonus_condition": lambda h, w, p, o: p == "green"},
    {"id": 3, "name": "Shubman Gill", "average": 57.0, "strike_rate": 102.0, "bonus_condition": lambda h, w, p, o: o > 7},
    {"id": 4, "name": "Yashasvi Jaiswal", "average": 45.0, "strike_rate": 105.0, "bonus_condition": lambda h, w, p, o: w > 15},
    {"id": 5, "name": "KL Rahul", "average": 50.0, "strike_rate": 87.0, "bonus_condition": lambda h, w, p, o: False}
]

# Generate balanced dataset with realistic distributions
n_rows = 500
rows_per_batter = n_rows // len(batters)  # ~100 rows per batter
data = {
    "humidity": [],  # Replaced temperature with humidity (30–90%)
    "wind_speed": [],
    "pitch_condition": [],
    "opposition_strength": [],
    "best_batter": []
}

for batter in batters:
    batter_id = batter["id"]
    for _ in range(rows_per_batter):
        # Generate realistic conditions favoring the batter
        if batter_id == 1:  # Kohli: dry pitch
            pitch = "dry"
            h = np.random.uniform(30, 90)
            w = np.random.uniform(0, 15)  # Lower wind speeds typical in India
            o = np.random.randint(1, 11)
        elif batter_id == 2:  # Rohit: green pitch
            pitch = "green"
            h = np.random.uniform(30, 90)
            w = np.random.uniform(0, 15)
            o = np.random.randint(1, 11)
        elif batter_id == 3:  # Gill: strong opposition
            pitch = np.random.choice(["green", "dry", "hard", "dusty"], p=[0.2, 0.4, 0.3, 0.1])  # Indian pitch bias
            h = np.random.uniform(30, 90)
            w = np.random.uniform(0, 15)
            o = np.random.randint(8, 11)  # Ensure o > 7
        elif batter_id == 4:  # Jaiswal: windy
            pitch = np.random.choice(["green", "dry", "hard", "dusty"], p=[0.2, 0.4, 0.3, 0.1])
            h = np.random.uniform(30, 90)
            w = np.random.uniform(15.1, 30)  # Ensure w > 15
            o = np.random.randint(1, 11)
        else:  # Rahul: no specific condition
            pitch = np.random.choice(["green", "dry", "hard", "dusty"], p=[0.2, 0.4, 0.3, 0.1])
            h = np.random.uniform(30, 90)
            w = np.random.uniform(0, 15)
            o = np.random.randint(1, 11)
        
        data["humidity"].append(h)
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
df.to_csv("cricket_knn_indian_players_improved.csv", index=False)
print("Improved dataset saved as 'cricket_knn_indian_players_improved.csv' with 500 rows.")