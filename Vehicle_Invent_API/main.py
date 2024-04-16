# Vehicle Inventory API
# Develop a FastAPI endpoint for managing vehicle inventory.
# ● Use path parameters for vehicle ID and query parameters for filtering by make,
# model, and price range.
# ● Apply numeric validation for vehicle ID and price range.
# ● Implement string validation for make and model parameters.
# ● Return details of a specific vehicle identified by ID or a list of vehicles based on
# the query parameters.
# ● Test the API with various combinations of parameters.

from fastapi import FastAPI, Query, Path, HTTPException
from models import Vehicle

app = FastAPI()

# Mock database of vehicles
vehicles_db = [
    {"id": 1, "make": "Toyota", "model": "Corolla", "price": 15000.0},
    {"id": 2, "make": "Honda", "model": "Civic", "price": 18000.0},
    {"id": 3, "make": "Ford", "model": "Focus", "price": 17000.0},
]

@app.get("/vehicles/{vehicle_id}")
async def get_vehicle_by_id(vehicle_id: int = Path(..., title="The ID of the vehicle to retrieve")):
    vehicle = next((v for v in vehicles_db if v["id"] == vehicle_id), None)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@app.get("/vehicles/")
async def get_vehicles(
    make: str = Query(None, title="Make of the vehicle"),
    model: str = Query(None, title="Model of the vehicle"),
    min_price: float = Query(None, gt=0, title="Minimum price of the vehicle"),
    max_price: float = Query(None, gt=0, title="Maximum price of the vehicle"),
):
    filtered_vehicles = vehicles_db

    if make:
        filtered_vehicles = [v for v in filtered_vehicles if v["make"].lower() == make.lower()]
    if model:
        filtered_vehicles = [v for v in filtered_vehicles if v["model"].lower() == model.lower()]
    if min_price is not None:
        filtered_vehicles = [v for v in filtered_vehicles if v["price"] >= min_price]
    if max_price is not None:
        filtered_vehicles = [v for v in filtered_vehicles if v["price"] <= max_price]

    return filtered_vehicles
