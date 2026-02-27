import joblib

def load_model():
    model = joblib.load("./notebooks/used_car_price_predictor_best_rf_model.pkl")
    return model