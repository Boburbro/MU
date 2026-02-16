# 📡 API Reference

Complete API endpoint documentation with examples.

## Base URL
```
http://localhost:8000
```

## Authentication

All endpoints except `/auth/login` require JWT token in header:
```
Authorization: Bearer <access_token>
```

---

## Authentication Endpoints

### POST /auth/login

Login user and get JWT token.

**Request:**
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

**Response:** `200 OK`
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "admin",
    "role": "admin"
  }
}
```

**Error Response:** `401 Unauthorized`
```json
{
  "detail": "Invalid username or password"
}
```

---

## Products Endpoints

### GET /products

List all products with pagination.

**Parameters:**
- `skip` (query, optional): Number of records to skip (default: 0)
- `limit` (query, optional): Max records to return (default: 100)

**Request:**
```bash
TOKEN="your_access_token"
curl -X GET "http://localhost:8000/products?skip=0&limit=10" \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Coca-Cola",
    "category": "Beverage",
    "price": 2.5,
    "stock_quantity": 50,
    "min_limit": 10
  },
  {
    "id": 2,
    "name": "Non (Water)",
    "category": "Beverage",
    "price": 1.0,
    "stock_quantity": 100,
    "min_limit": 20
  }
]
```

---

### GET /products/{id}

Get single product by ID.

**Parameters:**
- `id` (path, required): Product ID

**Request:**
```bash
curl -X GET http://localhost:8000/products/1 \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "Coca-Cola",
  "category": "Beverage",
  "price": 2.5,
  "stock_quantity": 50,
  "min_limit": 10
}
```

**Error Response:** `404 Not Found`
```json
{
  "detail": "Product not found"
}
```

---

### GET /products/low-stock

Get products below minimum limit.

**Request:**
```bash
curl -X GET http://localhost:8000/products/low-stock \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK`
```json
[
  {
    "id": 3,
    "name": "Yog' (Yogurt)",
    "category": "Dairy",
    "price": 3.5,
    "stock_quantity": 5,
    "min_limit": 10
  }
]
```

---

### POST /products

Create new product (Admin only).

**Request:**
```bash
curl -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "name": "Fresh Milk",
    "category": "Dairy",
    "price": 2.99,
    "stock_quantity": 50,
    "min_limit": 15
  }'
```

**Response:** `201 Created`
```json
{
  "id": 6,
  "name": "Fresh Milk",
  "category": "Dairy",
  "price": 2.99,
  "stock_quantity": 50,
  "min_limit": 15
}
```

**Error Response:** `403 Forbidden`
```json
{
  "detail": "This action requires one of these roles: admin"
}
```

---

### PUT /products/{id}

Update product (Admin only).

**Parameters:**
- `id` (path, required): Product ID

**Request:**
```bash
curl -X PUT http://localhost:8000/products/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "price": 3.0,
    "stock_quantity": 75
  }'
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "Coca-Cola",
  "category": "Beverage",
  "price": 3.0,
  "stock_quantity": 75,
  "min_limit": 10
}
```

---

### DELETE /products/{id}

Delete product (Admin only).

**Parameters:**
- `id` (path, required): Product ID

**Request:**
```bash
curl -X DELETE http://localhost:8000/products/1 \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `204 No Content`

---

## Sales Endpoints

### POST /sales

Record new sale (Staff & Admin).

**Request:**
```bash
curl -X POST http://localhost:8000/sales \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "product_id": 1,
    "quantity_sold": 5,
    "total_price": 15.00
  }'
```

**Response:** `201 Created`
```json
{
  "id": 101,
  "product_id": 1,
  "staff_id": 2,
  "quantity_sold": 5,
  "sale_date": "2025-01-22T10:30:45.123456",
  "total_price": 15.0
}
```

**Error Response:** `400 Bad Request`
```json
{
  "detail": "Invalid product or insufficient stock"
}
```

---

### GET /sales

Get sales history.

**Parameters:**
- `days` (query, optional): Days to look back (default: 30, max: 365)
- `skip` (query, optional): Records to skip (default: 0)
- `limit` (query, optional): Max records (default: 100)

**Request:**
```bash
curl -X GET "http://localhost:8000/sales?days=7&skip=0&limit=50" \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK`
```json
[
  {
    "id": 101,
    "product_id": 1,
    "staff_id": 2,
    "quantity_sold": 5,
    "sale_date": "2025-01-22T10:30:45.123456",
    "total_price": 15.0
  },
  {
    "id": 102,
    "product_id": 2,
    "staff_id": 2,
    "quantity_sold": 10,
    "sale_date": "2025-01-22T11:15:22.654321",
    "total_price": 10.0
  }
]
```

---

### GET /sales/today

Get today's sales.

**Request:**
```bash
curl -X GET http://localhost:8000/sales/today \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK`
```json
[
  {
    "id": 101,
    "product_id": 1,
    "staff_id": 2,
    "quantity_sold": 5,
    "sale_date": "2025-01-22T10:30:45.123456",
    "total_price": 15.0
  }
]
```

---

## Dashboard Endpoints

### GET /dashboard/summary

Get dashboard statistics and alerts.

**Request:**
```bash
curl -X GET http://localhost:8000/dashboard/summary \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK`
```json
{
  "total_products": 5,
  "low_stock_count": 1,
  "low_stock_products": [
    {
      "id": 3,
      "name": "Yog' (Yogurt)",
      "stock": 5,
      "min_limit": 10
    }
  ],
  "today_sales": {
    "count": 3,
    "total_quantity": 18,
    "total_revenue": 45.50
  }
}
```

---

## AI Prediction Endpoints

### GET /ai/predict

Get 7-day sales prediction for product.

**Parameters:**
- `product_id` (query, required): Product ID to predict

**Request:**
```bash
curl -X GET "http://localhost:8000/ai/predict?product_id=1" \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK`
```json
{
  "product_id": 1,
  "product_name": "Coca-Cola",
  "current_stock": 45,
  "prediction": {
    "method": "linear_regression",
    "daily_predictions": [3, 4, 3, 4, 5, 3, 4],
    "total_7days": 26,
    "daily_average": 3.7,
    "confidence": "high"
  }
}
```

**Error Response:** `404 Not Found`
```json
{
  "detail": "Product not found"
}
```

---

### GET /ai/reorder-suggestion

Get reorder suggestion based on prediction.

**Parameters:**
- `product_id` (query, required): Product ID

**Request:**
```bash
curl -X GET "http://localhost:8000/ai/reorder-suggestion?product_id=1" \
  -H "Authorization: Bearer $TOKEN"
```

**Response:** `200 OK` (Good Stock)
```json
{
  "product_id": 1,
  "product_name": "Coca-Cola",
  "recommendation": "No reorder needed",
  "reason": "Current stock (45) covers predicted demand",
  "quantity": 0,
  "urgency": "low"
}
```

**Response:** `200 OK` (Need Reorder)
```json
{
  "product_id": 3,
  "product_name": "Yog' (Yogurt)",
  "recommendation": "Reorder 25 units",
  "reason": "Predicted 7-day sales: 20, Current: 5",
  "quantity": 25,
  "urgency": "high",
  "prediction": {
    "method": "linear_regression",
    "daily_predictions": [2, 3, 3, 2, 3, 3, 4],
    "total_7days": 20,
    "daily_average": 2.9,
    "confidence": "medium"
  }
}
```

---

## Utility Endpoints

### GET /

Get API information.

**Request:**
```bash
curl -X GET http://localhost:8000/
```

**Response:** `200 OK`
```json
{
  "name": "Smart Inventory API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

---

### GET /health

Health check endpoint.

**Request:**
```bash
curl -X GET http://localhost:8000/health
```

**Response:** `200 OK`
```json
{
  "status": "ok"
}
```

---

### GET /docs

Interactive Swagger UI documentation.

**Request:**
```
Open in browser: http://localhost:8000/docs
```

---

### GET /redoc

ReDoc API documentation.

**Request:**
```
Open in browser: http://localhost:8000/redoc
```

---

## Error Responses

### Common Error Codes

| Code | Status | Meaning |
|------|--------|---------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 204 | No Content | Successful deletion |
| 400 | Bad Request | Invalid input data |
| 401 | Unauthorized | Missing or invalid token |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 422 | Unprocessable Entity | Validation error |
| 500 | Internal Server Error | Server error |

### Standard Error Response

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Validation Error Response

```json
{
  "detail": [
    {
      "loc": ["body", "price"],
      "msg": "ensure this value is greater than 0",
      "type": "value_error.number.not_gt"
    }
  ]
}
```

---

## Rate Limiting & Throttling

Currently no rate limiting is implemented. For production:
- Implement 100 requests/minute per IP
- 1000 requests/hour per authenticated user
- Use Redis for rate limiting

---

## Pagination

List endpoints support pagination:

```bash
# Get records 10-20
curl -X GET "http://localhost:8000/products?skip=10&limit=10" \
  -H "Authorization: Bearer $TOKEN"
```

**Parameters:**
- `skip`: Number of records to skip (offset)
- `limit`: Maximum records to return (1-100)

---

## Filtering & Sorting

Currently supported:
- Get low-stock products: `GET /products/low-stock`
- Filter sales by date range: `GET /sales?days=7`
- Get today's sales: `GET /sales/today`

Future improvements:
- Product category filtering
- Date range filtering on sales
- Sorting options

---

## Testing API with cURL

### Full Example Workflow

```bash
# 1. Login
RESPONSE=$(curl -s -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}')

TOKEN=$(echo $RESPONSE | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)

# 2. Get products
curl -X GET http://localhost:8000/products \
  -H "Authorization: Bearer $TOKEN"

# 3. Get prediction for product 1
curl -X GET "http://localhost:8000/ai/predict?product_id=1" \
  -H "Authorization: Bearer $TOKEN"

# 4. Get reorder suggestion
curl -X GET "http://localhost:8000/ai/reorder-suggestion?product_id=1" \
  -H "Authorization: Bearer $TOKEN"
```

---

## API Response Times

Expected response times (on local machine):
- Login: ~50ms
- Get products: ~30ms
- Create product: ~40ms
- Get prediction: ~200ms (first time), ~50ms (cached)
- Get dashboard: ~100ms

---

**API Version:** 1.0.0  
**Last Updated:** January 2025  
**Status:** Production Ready MVP
