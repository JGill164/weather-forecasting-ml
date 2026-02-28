import pandas as pd

df = pd.read_csv(
    "vancouver_rainfall_raw.csv",
    skiprows=9,
    usecols=["YEAR","JAN","FEB","MAR","APR","MAY","JUN", "JUL","AUG","SEP","OCT","NOV","DEC"]
)

#reorganize
df_long = df.melt(
    id_vars=["YEAR"],
    var_name="month",
    value_name="rainfall_mm"
)

#assign int
month_map = {
    "JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6, "JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12
}
df_long["month"] = df_long["month"].map(month_map)

df_long["date"] = pd.to_datetime(
    df_long["YEAR"].astype(str) + "-" + df_long["month"].astype(str),
    format="%Y-%m"
)

df_long = df_long.sort_values("date")
df_final = df_long[["date","rainfall_mm"]].reset_index(drop=True)

df_final.to_csv("vancouver_rainfall_clean.csv", index=False)

print(df_final.head())

