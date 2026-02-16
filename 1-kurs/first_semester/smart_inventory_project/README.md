# 📦 Smart Inventory Management System

MVP (Minimum Viable Product) for inventory management with AI-powered sales prediction.

## 🎯 Features

- **Authentication**: JWT-based login with role-based access control (Admin/Staff)
- **Product Management**: CRUD operations for inventory products
- **Sales Tracking**: Record and view sales transactions
- **Dashboard**: Real-time inventory statistics and low-stock alerts
- **AI Prediction**: 7-day sales forecast using scikit-learn LinearRegression
- **Reorder Suggestions**: Automatic reorder recommendations based on predictions

## 📋 Tech Stack

### Backend
- **Framework**: FastAPI 0.104.1
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT (python-jose)
- **Password**: bcrypt hashing
- **AI/ML**: scikit-learn LinearRegression
- **Validation**: Pydantic

### Frontend
- **Framework**: React 18.2.0
- **Routing**: React Router v6
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios with interceptors
- **Build Tool**: Vite

## 🚀 Quick Start

### Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Run server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server will be available at `http://localhost:8000`
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Run development server
npm run dev
```

Frontend will be available at `http://localhost:5173`

## 🔐 Default Credentials

| User | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| Staff | `staff` | `staff123` |

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hashed VARCHAR(255) NOT NULL,
  role VARCHAR(10) NOT NULL  -- 'admin' or 'staff'
);
```

### Products Table
```sql
CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  category VARCHAR(50) NOT NULL,
  price FLOAT NOT NULL,
  stock_quantity INTEGER NOT NULL,
  min_limit INTEGER NOT NULL
);
```

### Sales Table
```sql
CREATE TABLE sales (
  id INTEGER PRIMARY KEY,
  product_id INTEGER NOT NULL FOREIGN KEY,
  staff_id INTEGER NOT NULL FOREIGN KEY,
  quantity_sold INTEGER NOT NULL,
  sale_date DATETIME NOT NULL,
  total_price FLOAT NOT NULL
);
```

## 🔌 API Endpoints

### Authentication
- `POST /auth/login` - User login, returns JWT token

### Products (requires JWT)
- `GET /products` - List all products (Admin & Staff)
- `GET /products/{id}` - Get single product
- `GET /products/low-stock` - Get low stock products
- `POST /products` - Create product (Admin only)
- `PUT /products/{id}` - Update product (Admin only)
- `DELETE /products/{id}` - Delete product (Admin only)

### Sales (requires JWT)
- `POST /sales` - Record new sale (Staff & Admin)
- `GET /sales` - Get sales history
- `GET /sales/today` - Get today's sales

### Dashboard (requires JWT)
- `GET /dashboard/summary` - Get statistics and alerts

### AI Predictions (requires JWT)
- `GET /ai/predict?product_id=ID` - Get 7-day sales prediction
- `GET /ai/reorder-suggestion?product_id=ID` - Get reorder suggestion

## 📄 Sample API Requests

### 1. Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

**Response:**
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

### 2. Get Products
```bash
curl -X GET http://localhost:8000/products \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Coca-Cola",
    "category": "Beverage",
    "price": 2.5,
    "stock_quantity": 50,
    "min_limit": 10
  }
]
```

### 3. Record Sale
```bash
curl -X POST http://localhost:8000/sales \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "product_id": 1,
    "quantity_sold": 5,
    "total_price": 12.50
  }'
```

### 4. AI Prediction
```bash
curl -X GET "http://localhost:8000/ai/predict?product_id=1" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Response:**
```json
{
  "product_id": 1,
  "product_name": "Coca-Cola",
  "current_stock": 45,
  "prediction": {
    "method": "linear_regression",
    "daily_predictions": [3, 4, 3, 2, 3, 4, 5],
    "total_7days": 24,
    "daily_average": 3.2,
    "confidence": "high"
  }
}
```

## 🧪 Running Tests

```bash
cd backend

# Run pytest
pytest test_api.py -v

# Run specific test
pytest test_api.py::TestAuth::test_login_admin -v
```

## 📱 Frontend Pages

### Login Page
- Username/Password input
- Shows test credentials
- Stores JWT token in localStorage
- Redirects to dashboard on success

### Dashboard
- Summary cards (Total Products, Low Stock, Today's Sales)
- Low stock alerts table
- 7-day sales prediction widget
- AI chart visualization

### Inventory Management
- Products table with filtering
- Create/Edit/Delete products (Admin only)
- Record sales modal
- Stock status indicators

## 🤖 AI Predictor Details

### Algorithm
- Uses `scikit-learn LinearRegression`
- Trains on historical sales data from last 30 days
- Predicts quantity sold for next 7 days

### Confidence Levels
- **High**: If 14+ days of history available
- **Medium**: If 2-13 days of history available
- **Low**: If less than 2 days of history (uses average)

### Reorder Logic
- Calculates: `Required = PredictedTotal + SafetyBuffer(20%) - CurrentStock`
- Urgency set to "high" if current stock < min_limit
- Returns 0 if stock is sufficient

## 📁 Project Structure

```
smart_inventory_project/
├── backend/
│   ├── app/
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── crud/          # Database operations
│   │   ├── routes/        # API endpoints
│   │   ├── services/      # Business logic (AI, etc)
│   │   ├── middleware/    # Auth middleware
│   │   ├── utils/         # Helpers
│   │   └── main.py        # FastAPI app
│   ├── requirements.txt
│   ├── .env.example
│   └── test_api.py
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── services/      # API calls
│   │   └── App.jsx
│   ├── package.json
│   └── tailwind.config.js
└── README.md
```

## ✅ MVP Checklist

- [x] Backend Setup (FastAPI + SQLAlchemy + SQLite)
- [x] Database Models (Users, Products, Sales)
- [x] JWT Authentication
- [x] Role-Based Access Control
- [x] Product CRUD Operations
- [x] Sales Recording
- [x] Dashboard Summary
- [x] AI Sales Prediction (LinearRegression)
- [x] Reorder Suggestions
- [x] Frontend Pages (Login, Dashboard, Inventory)
- [x] API Client with Interceptors
- [x] Protected Routes
- [x] Seed Data (Admin/Staff users + Sample products)
- [x] API Testing Examples
- [x] CORS Configuration
- [x] Error Handling & Validation

## 🔒 Security Notes

1. Change `JWT_SECRET` in production
2. Use HTTPS in production
3. Set `DEBUG=False` in production
4. Use environment variables for sensitive data
5. Implement rate limiting for production
6. Use secure password policies

## 📝 Environment Variables

### Backend (.env)
```
DATABASE_URL=sqlite:///./smart_inventory.db
JWT_SECRET=your-super-secret-key
JWT_ALGORITHM=HS256
DEBUG=True
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000
```

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Backend
lsof -i :8000
kill -9 <PID>

# Frontend
lsof -i :5173
kill -9 <PID>
```

**Database issues:**
```bash
# Delete database and reseed
rm backend/smart_inventory.db
# Restart backend
```

**CORS errors:**
Make sure backend is running and VITE_API_URL is correct in frontend .env

## 📚 Documentation

- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **ReDoc**: http://localhost:8000/redoc
- **Test Examples**: See `backend/test_api.py`

## 🎓 Learning Resources

- FastAPI: https://fastapi.tiangolo.com/
- React: https://react.dev/
- SQLAlchemy: https://www.sqlalchemy.org/
- Tailwind CSS: https://tailwindcss.com/
- scikit-learn: https://scikit-learn.org/

---

**Created**: January 2026  
**Version**: 1.0.0 MVP
