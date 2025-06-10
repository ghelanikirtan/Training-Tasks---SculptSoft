import pandas as pd
import numpy as np

# Define Indian batters with real stats
batters = [
    {"id": 1, "name": "Virat Kohli", "average": 58.0, "strike_rate": 93.0, "bonus_condition": lambda t, w, p, o: p == "dry"},
    {"id": 2, "name": "Rohit Sharma", "average": 49.0, "strike_rate": 90.0, "bonus_condition": lambda t, w, p, o: p == "green"},
    {"id": 3, "name": "Shubman Gill", "average": 57.0, "strike_rate": 102.0, "bonus_condition": lambda t, w, p, o: o > 7},
    {"id": 4, "name": "Yashasvi Jaiswal", "average": 45.0, "strike_rate": 105.0, "bonus_condition": lambda t, w, p, o: w > 15},
    {"id": 5, "name": "KL Rahul", "average": 50.0, "strike_rate": 87.0, "bonus_condition": lambda t, w, p, o: False}
]

# Generate dataset
n_rows = 500
data = {
    "temperature": np.random.uniform(15, 40, n_rows),
    "wind_speed": np.random.uniform(0, 30, n_rows),
    "pitch_condition": np.random.choice(["green", "dry", "hard", "dusty"], n_rows),
    "opposition_strength": np.random.randint(1, 11, n_rows)
}

df = pd.DataFrame(data)

# One-hot encode pitch_condition
pitch_dummies = pd.get_dummies(df["pitch_condition"], prefix="pitch")
df = pd.concat([df, pitch_dummies], axis=1)
df = df.drop("pitch_condition", axis=1)

# Calculate best batter for each row
best_batters = []
for i in range(n_rows):
    t, w, o = df.iloc[i]["temperature"], df.iloc[i]["wind_speed"], df.iloc[i]["opposition_strength"]
    p = "green" if df.iloc[i]["pitch_green"] else "dry" if df.iloc[i]["pitch_dry"] else "hard" if df.iloc[i]["pitch_hard"] else "dusty"
    scores = []
    for batter in batters:
        bonus = 0.1 if batter["bonus_condition"](t, w, p, o) else 0
        noise = np.random.uniform(-5, 5)
        score = batter["average"] * (1 + bonus) + noise
        scores.append((batter["id"], score))
    best_batter = max(scores, key=lambda x: x[1])[0]
    best_batters.append(best_batter)

df["best_batter"] = best_batters

# Save to CSV
df.to_csv("./datasets/cricket_knn_indian_players.csv", index=False)
print("Dataset saved as 'cricket_knn_indian_players.csv' with 500 rows.")