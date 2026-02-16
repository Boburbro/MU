"""
API Test Examples - Run with: pytest test_api.py
Or manually test with curl commands below
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine
import requests

client = TestClient(app)

# Test data
TEST_ADMIN = {"username": "admin", "password": "admin123"}
TEST_STAFF = {"username": "staff", "password": "staff123"}

class TestAuth:
    def test_login_admin(self):
        """Test admin login"""
        response = client.post("/auth/login", json=TEST_ADMIN)
        assert response.status_code == 200
        assert "access_token" in response.json()
        assert response.json()["user"]["role"] == "admin"

    def test_login_staff(self):
        """Test staff login"""
        response = client.post("/auth/login", json=TEST_STAFF)
        assert response.status_code == 200
        assert "access_token" in response.json()
        assert response.json()["user"]["role"] == "staff"

    def test_login_invalid(self):
        """Test invalid login"""
        response = client.post("/auth/login", json={"username": "invalid", "password": "wrong"})
        assert response.status_code == 401

class TestProducts:
    @pytest.fixture
    def admin_token(self):
        response = client.post("/auth/login", json=TEST_ADMIN)
        return response.json()["access_token"]

    def test_get_products(self, admin_token):
        """Test get all products"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = client.get("/products", headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_create_product(self, admin_token):
        """Test create product (admin only)"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        new_product = {
            "name": "Test Product",
            "category": "Test",
            "price": 9.99,
            "stock_quantity": 50,
            "min_limit": 10
        }
        response = client.post("/products", json=new_product, headers=headers)
        assert response.status_code == 201
        assert response.json()["name"] == "Test Product"

    def test_low_stock_products(self, admin_token):
        """Test get low stock products"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = client.get("/products/low-stock", headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

class TestDashboard:
    @pytest.fixture
    def staff_token(self):
        response = client.post("/auth/login", json=TEST_STAFF)
        return response.json()["access_token"]

    def test_dashboard_summary(self, staff_token):
        """Test dashboard summary"""
        headers = {"Authorization": f"Bearer {staff_token}"}
        response = client.get("/dashboard/summary", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert "total_products" in data
        assert "low_stock_count" in data
        assert "today_sales" in data

# CURL Examples (run these manually in terminal)
"""
# 1. Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

# Expected Response:
# {
#   "access_token": "eyJhbGc...",
#   "token_type": "bearer",
#   "user": {"id": 1, "username": "admin", "role": "admin"}
# }

# 2. Get Products (save token from login response)
curl -X GET http://localhost:8000/products \
  -H "Authorization: Bearer <YOUR_TOKEN>"

# 3. Create Product (admin only)
curl -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -d '{
    "name": "New Product",
    "category": "Electronics",
    "price": 29.99,
    "stock_quantity": 100,
    "min_limit": 20
  }'

# 4. Record Sale (staff can do this)
curl -X POST http://localhost:8000/sales \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -d '{
    "product_id": 1,
    "quantity_sold": 5,
    "total_price": 12.50
  }'

# 5. Get AI Prediction
curl -X GET "http://localhost:8000/ai/predict?product_id=1" \
  -H "Authorization: Bearer <YOUR_TOKEN>"

# 6. Get Reorder Suggestion
curl -X GET "http://localhost:8000/ai/reorder-suggestion?product_id=1" \
  -H "Authorization: Bearer <YOUR_TOKEN>"

# 7. Get Dashboard Summary
curl -X GET http://localhost:8000/dashboard/summary \
  -H "Authorization: Bearer <YOUR_TOKEN>"
"""
