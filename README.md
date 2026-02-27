# Used Car Price Prediction API

A modern, modular FastAPI-based backend and simple frontend for predicting the price of used cars and comparing two cars using a machine learning model.

## Features
- Predict the selling price of a used car based on its features
- Compare two cars and get their predicted prices, price difference, and which is cheaper
- RESTful API built with FastAPI
- Frontend for user interaction (HTML/JS/CSS)
- Modular backend structure for maintainability

## Project Structure
```
car_price_prediction/
├── backend/
│   ├── app.py            # FastAPI app and API routes
│   ├── model.py          # Model loading and business logic
│   ├── schemas.py        # Pydantic models for request/response
│   └── ...
├── datasets/
│   └── cardekho_dataset.csv
├── frontend/
│   ├── index.html        # Main UI
│   ├── script.js         # Frontend logic
│   └── styles.css        # Styling
├── notebooks/
│   └── notebook.ipynb    # Model training and exploration
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project metadata
├── main.py, predict.py   # (If used) Entry points or scripts
└── README.md             # Project documentation
```

## API Endpoints

### Health Check
- `GET /` — Returns a simple status message.

### Predict Car Price
- `POST /predict/`
  - **Request Body:** Car features (see below)
  - **Response:** Predicted selling price

### Compare Two Cars
- `POST /compare/`
  - **Request Body:** Features for two cars
  - **Response:** Predicted prices, price difference, and cheaper car

#### Example Car Features JSON
```json
{
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
```

## Setup & Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Model Path (Optional)
By default, the model is loaded from `./notebooks/used_car_price_predictor_best_rf_model.pkl`. To override, set the `MODEL_PATH` environment variable.

### 3. Run the Backend
```bash
cd backend
uvicorn app:app --reload
```

### 4. Access the Frontend
Open `frontend/index.html` in your browser.

### 5. API Documentation
Once the backend is running, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

## Notes
- Ensure the trained model file exists at the specified path.
- The backend is modular: business logic is in `model.py`, API routes in `app.py`, and data schemas in `schemas.py`.
- For further model training or exploration, use the Jupyter notebook in `notebooks/`.

## License
This project is for educational and demonstration purposes.
