# Weather Forecasting – Vancouver Rainfall

Time series forecasting project using Random Forest regression and lag-based feature engineering.

## Problem
Predict monthly rainfall using historical rainfall data.

## Feature Engineering
- lag_1 (previous month)
- lag_2 (2 months back)
- lag_12 (same month last year)

## Model
RandomForestRegressor (200 trees)

## Evaluation
- MAE: 63.85 
- Baseline (lag_12): 73.51

Model outperforms naive seasonal baseline.

## Tableau Dashboard

The visualization below shows historical rainfall in Vancouver alongside a 5-year forecast generated using a Random Forest regression model.

A vertical reference line marks the forecast start (January 2026).

![Rainfall Forecast](tableau/dashboard.png)