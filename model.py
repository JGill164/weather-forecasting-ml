import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("vancouver_rainfall_clean.csv")
df["date"] = pd.to_datetime(df["date"])

#sort
df = df.sort_values("date")

df["lag_1"] = df["rainfall_mm"].shift(1)
df["lag_2"] = df["rainfall_mm"].shift(2)
df["lag_12"] = df["rainfall_mm"].shift(12)

# Drop missing rows from shifting
df = df.dropna()

# Features and target
X = df[["lag_1", "lag_2", "lag_12"]]
y = df["rainfall_mm"]

# Train/test split
split_index = int(len(df) * 0.8)

X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Train model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)

print("MAE:", mae)

baseline_pred = X_test["lag_12"].values
baseline_mae = mean_absolute_error(y_test, baseline_pred)
print("Baseline MAE (lag_12):", baseline_mae)