from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_products_no_params():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Laptop", "category": "Electronics", "price": 1200.50},
        {"name": "Headphones", "category": "Electronics", "price": 99.99},
        {"name": "T-shirt", "category": "Clothing", "price": 19.99},
        {"name": "Sneakers", "category": "Shoes", "price": 59.99}
    ]

def test_search_products_with_name():
    response = client.get("/products/?name=Laptop")
    assert response.status_code == 200
    assert response.json() == [{"name": "Laptop", "category": "Electronics", "price": 1200.50}]

def test_search_products_with_category():
    response = client.get("/products/?category=Electronics")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Laptop", "category": "Electronics", "price": 1200.50},
        {"name": "Headphones", "category": "Electronics", "price": 99.99}
    ]