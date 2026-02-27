import numpy as np
import pandas as pd
from model import load_model
from schemas import CarFeatures, SellingPrice

model = load_model()

def predict(features: CarFeatures) -> SellingPrice:
    df = pd.DataFrame([features.model_dump()])
    pred_log = model.predict(df)
    pred_price = np.expm1(pred_log[0])
    return SellingPrice(selling_price=pred_price)