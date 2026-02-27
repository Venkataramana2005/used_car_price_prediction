import pandas as pd
import numpy as np
from model import load_model
from schemas import CompareCarsRequest, ComparisionResult

model = load_model()

def compare_cars(cars: CompareCarsRequest) -> ComparisionResult:
    df1 = pd.DataFrame([cars.car1.model_dump()])
    pred1_log = model.predict(df1)
    price1 = float(np.expm1(pred1_log)[0])

    df2 = pd.DataFrame([cars.car2.model_dump()])
    pred2_log = model.predict(df2)
    price2 = float(np.expm1(pred2_log)[0])

    price_diff = abs(price1 - price2)
    cheaper = cars.car1.car_name if price1 < price2 else cars.car2.car_name

    return ComparisionResult(
        car1_name = cars.car1.car_name,
        car1_price = round(price1,2),
        car2_name = cars.car2.car_name,
        car2_price = round(price2,2),
        price_difference = round(price_diff,2),
        cheaper_car = cheaper
    )