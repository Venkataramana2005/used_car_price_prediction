import numpy as np
import pandas as pd
import joblib
import time

start_time = time.time()
model = joblib.load("./notebooks/used_car_price_predictor_best_rf_model.pkl")
print(model)

new_car = pd.DataFrame([{
    "car_name": "Maruti Alto",
    "brand": "Maruti",
    "model": "Alto",
    "vehicle_age": 1,
    "km_driven": 150000,
    "seller_type": "Dealer",
    "fuel_type": "Diesel",
    "transmission_type": "Manual",
    "mileage": 15.89,
    "engine": 790,
    "max_power": 58.96,
    "seats": 5,
}])
pred_log = model.predict(new_car)
pred_price = np.expm1(pred_log)
end_time = time.time()
print(f"Predicted Selling Price: Rs.{pred_price[0]:,.2f} Response Time: {end_time-start_time}")
