# Product Search API:
# ● Develop a FastAPI endpoint for searching products.
# ● Accept query parameters for product name, category, and price range.
# ● Implement string validation for product name and category.
# ● Apply numeric validation for price range parameters.
# ● Return a list of products matching the search criteria.
# ● Test the API with various combinations of query parameters.

from fastapi import FastAPI, Query
from typing import List, Optional   
from models import Product

app = FastAPI()


products_db = [
    {"name": "Laptop", "category": "Electronics", "price": 1200.50},
    {"name": "Headphones", "category": "Electronics", "price": 99.99},
    {"name": "T-shirt", "category": "Clothing", "price": 19.99},
    {"name": "Sneakers", "category": "Shoes", "price": 59.99},
]

@app.get("/products/", 
         summary="Search Products",
         description="Search for products based on optional query parameters: name, category, min_price, and max_price.",
         response_description="List of products matching the search criteria",
         response_model=List[Product]
        )
async def search_products(
    name: Optional[str] = Query(None, description="Name of the product"),
    category: Optional[str] = Query(None, description="Category of the product"),
    min_price: Optional[float] = Query(None, gt=0, description="Minimum price of the product"),
    max_price: Optional[float] = Query(None, gt=0, description="Maximum price of the product"),
):
    """
    Search for products based on the provided query parameters.
    
    Parameters:
    - name: Name of the product (optional).
    - category: Category of the product (optional).
    - min_price: Minimum price of the product (optional).
    - max_price: Maximum price of the product (optional).
    
    Returns:
    - List of products matching the search criteria.
    """
    filtered_products = products_db

    if name:
        filtered_products = [p for p in filtered_products if name.lower() in p["name"].lower()]
    if category:
        filtered_products = [p for p in filtered_products if category.lower() == p["category"].lower()]
    if min_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] >= min_price]
    if max_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] <= max_price]

    return filtered_products
