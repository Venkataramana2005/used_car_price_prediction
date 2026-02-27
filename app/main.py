import numpy as np
import pandas as pd
import joblib
from model import load_model
from comparision import compare_cars
from predict import predict
from schemas import CarFeatures, SellingPrice, CompareCarsRequest, ComparisionResult
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Used Car Price Predictor",
    summary="This API predicts the car price which are used"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model()

@app.get("/")
async def home():
    return {"Message": "Predictor is Good!"}

@app.post("/predict/",response_model=SellingPrice)
async def predict_price(features: CarFeatures) -> SellingPrice:
    try:
        return predict(features)
    except Exception as e:
        raise HTTPException(status_code=500,detail="Prediction Error: {str(e)}")

@app.post("/compare/",response_model=ComparisionResult)
async def compare_cars_price(cars: CompareCarsRequest) -> ComparisionResult:
    try:
        return compare_cars(cars)
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Comparision Error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)