from typing import Literal
from pydantic import BaseModel, Field, field_validator, ConfigDict

class CarFeatures(BaseModel):
    car_name: str = Field(title="Name of the car",min_length=1,max_length=50)
    brand: str = Field(title="car Brand")
    model: str = Field(title="Car model")
    vehicle_age: int = Field(description="years completed since car buyed",ge=1,le=30)
    km_driven: int = Field(description="No of kilometers car has travelled",ge=100,le=5000000)
    seller_type: Literal["Dealer","Individual","Trusted Dealer"] = "Dealer"
    fuel_type: Literal["Diesel","Petrol"] = "Diesel"
    transmission_type: Literal["Manual","Automatic"] = "Manual"
    mileage: float = Field(description="Mileage of the car",ge=1,le=100)
    engine: int = Field(description="It is the engine capacity in cc(cubic centimeters)",ge=100,le=10000)
    max_power: float = Field(description="Max power it produces in BHP",ge=10,le=1000)
    seats: int = Field(description="No of seats in car",ge=2,le=10)

    @field_validator("brand","model",mode="before")
    @classmethod
    def caplitalize_feature(cls, value:str) -> str:
        return value.title()

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
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
                "seats": 5
                }
            }
        )

class SellingPrice(BaseModel):
    selling_price: float = Field(description="Selling price of a car",ge=0)

class CompareCarsRequest(BaseModel):
    car1: CarFeatures
    car2: CarFeatures

class ComparisionResult(BaseModel):
    car1_name: str = Field(title="Name of the car",min_length=1,max_length=50)
    car1_price: float = Field(description="Selling price of a car",ge=0)
    car2_name: str = Field(title="Name of the car",min_length=1,max_length=50)
    car2_price: float = Field(description="Selling price of a car",ge=0)
    price_difference: float = Field(description="Price Difference between cars",ge=0)
    cheaper_car: str = Field(title="Cheaper Car",min_length=1,max_length=50)