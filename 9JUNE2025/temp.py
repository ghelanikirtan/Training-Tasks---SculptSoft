
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSVs (upload via Colab if needed)
odb = pd.read_csv("odb.csv")
tb = pd.read_csv("tb.csv")
twb = pd.read_csv("twb.csv")

# Clean & tag format
def clean_batting(df, format_name):
    df = df.rename(columns=lambda x: x.strip())
    df['Format'] = format_name
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')
    return df

odb = clean_batting(odb, 'ODI')
tb = clean_batting(tb, 'Test')
twb = clean_batting(twb, 'T20')

batting_df = pd.concat([odb, tb, twb], ignore_index=True)

# Convert numerics
cols = ['Mat', 'Inns', 'NO', 'Runs', 'Ave', 'BF', 'SR', '100', '50', '0', '4s', '6s']
for col in cols:
    batting_df[col] = pd.to_numeric(batting_df[col], errors='coerce')

# Create new features
batting_df["Boundary_Runs"] = batting_df["4s"] * 4 + batting_df["6s"] * 6
batting_df["Boundary_Perc"] = batting_df["Boundary_Runs"] / batting_df["Runs"]
batting_df["Aggression_Index"] = batting_df["SR"] * (batting_df["100"] + batting_df["50"]) / batting_df["Inns"]
batting_df["Consistency"] = batting_df["Ave"] * (batting_df["Inns"] - batting_df["0"]) / batting_df["Inns"]

batting_df = batting_df.dropna(subset=["Runs", "Ave", "SR"])


# Top 10 Run Scorers
top = batting_df.sort_values("Runs", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(data=top, y="Player", x="Runs", hue="Format")
plt.title("Top 10 Run Scorers")
plt.show()

# Aggression vs Consistency
plt.figure(figsize=(10, 6))
sns.scatterplot(data=batting_df, x="Consistency", y="Aggression_Index", hue="Format", size="Runs", sizes=(20, 200))
plt.title("Aggression vs Consistency")
plt.show()

# Select features
features = ["Mat", "Inns", "NO", "Runs", "Ave", "SR", "100", "50", "0", "4s", "6s", "Boundary_Perc", "Aggression_Index", "Consistency"]
df_model = batting_df[features].dropna()

# Optional: Normalize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(df_model)


# Example: Based on Aggression + SR, assign role (Opener, Middle, Finisher)
def assign_role(row):
    if row["SR"] >= 120 and row["Aggression_Index"] >= 60:
        return "Finisher"
    elif row["Consistency"] > 35 and row["SR"] > 90:
        return "Opener"
    else:
        return "Middle"

batting_df["Role"] = batting_df.apply(assign_role, axis=1)
df_model["Role"] = batting_df["Role"]



from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

X = df_model.drop(columns="Role")
y = df_model["Role"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

