import pandas as pd
from sklearn.ensemble import RandomForestRegressor

#load
df = pd.read_csv("vancouver_rainfall_clean.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date").reset_index(drop=True)

#lag
df["lag_1"] = df["rainfall_mm"].shift(1)
df["lag_2"] = df["rainfall_mm"].shift(2)
df["lag_12"] = df["rainfall_mm"].shift(12)
df_model = df.dropna().copy()

X = df_model[["lag_1", "lag_2", "lag_12"]]
y = df_model["rainfall_mm"]

#training
model = RandomForestRegressor(n_estimators=400, random_state=42)
model.fit(X, y)

#60 months ahead
history = df[["date", "rainfall_mm"]].copy()
last_date = history["date"].max()

future = []
for step in range(1, 61):
    next_date = last_date + pd.DateOffset(months=step)

    #grab lags
    lag_1 = history.iloc[-1]["rainfall_mm"]
    lag_2 = history.iloc[-2]["rainfall_mm"]
    lag_12 = history.iloc[-12]["rainfall_mm"]

    x_next = pd.DataFrame([{"lag_1": lag_1, "lag_2": lag_2, "lag_12": lag_12}])
    pred = float(model.predict(x_next)[0])

    future.append({"date": next_date, "rainfall_pred_mm": pred, "horizon_month": step})

    history = pd.concat([history, pd.DataFrame([{"date": next_date, "rainfall_mm": pred}])], ignore_index=True)

forecast_df = pd.DataFrame(future)
forecast_df.to_csv("vancouver_rainfall_forecast_5y.csv", index=False)
print("Saved: vancouver_rainfall_forecast_5y.csv")
print(forecast_df.head())