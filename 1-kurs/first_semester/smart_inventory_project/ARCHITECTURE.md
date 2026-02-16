# 🏗️ Smart Inventory System - Architecture Guide

## Project Overview

**Smart Inventory** is a full-stack MVP (Minimum Viable Product) for warehouse inventory management with AI-powered sales forecasting. It follows a three-tier architecture: Frontend (React), Backend (FastAPI), and Database (SQLite).

---

## 📊 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE (React)                    │
│  ┌──────────────┐  ┌─────────────┐  ┌────────────────────────┐ │
│  │  Login Page  │  │ Dashboard   │  │  Inventory Manager     │ │
│  │  (Auth)      │  │ (Stats +    │  │  (CRUD + Sales)        │ │
│  │              │  │  Predict)   │  │                        │ │
│  └──────────────┘  └─────────────┘  └────────────────────────┘ │
└──────────────────────┬──────────────────────────────────────────┘
                       │ HTTP/REST API
                       │ (JWT Authorization)
┌──────────────────────▼──────────────────────────────────────────┐
│                   BACKEND API (FastAPI)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │   AUTH       │  │  PRODUCTS    │  │  SALES & DASHBOARD   │  │
│  │  • Login     │  │  • CRUD Ops  │  │  • Record Transactions
│  │  • JWT Gen   │  │  • Validation│  │  • Get Statistics    │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  AI/ML SERVICE (scikit-learn LinearRegression)          │  │
│  │  • Historical Data Analysis                              │  │
│  │  • 7-Day Sales Prediction                                │  │
│  │  • Reorder Suggestions                                   │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  MIDDLEWARE & UTILITIES                                  │  │
│  │  • JWT Verification & Role-Based Access                  │  │
│  │  • CORS Handling                                         │  │
│  │  • Error Handling                                        │  │
│  │  • Password Hashing (bcrypt)                             │  │
│  └──────────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────────┘
                       │ SQLAlchemy ORM
┌──────────────────────▼──────────────────────────────────────────┐
│               DATABASE (SQLite)                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────────────┐    │
│  │ USERS       │  │ PRODUCTS    │  │ SALES                │    │
│  │ • id        │  │ • id        │  │ • id                 │    │
│  │ • username  │  │ • name      │  │ • product_id (FK)    │    │
│  │ • password  │  │ • category  │  │ • staff_id (FK)      │    │
│  │ • role      │  │ • price     │  │ • quantity_sold      │    │
│  │             │  │ • stock     │  │ • sale_date          │    │
│  │             │  │ • min_limit │  │ • total_price        │    │
│  └─────────────┘  └─────────────┘  └──────────────────────┘    │
│  Keys: username UNIQUE, Foreign Keys on products & sales       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Directory Structure & File Organization

### Backend Directory Tree

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI Application entrypoint
│   ├── config.py               # Configuration (DB URL, JWT secret, CORS)
│   ├── database.py             # SQLAlchemy setup (engine, session, Base)
│   │
│   ├── models/                 # SQLAlchemy ORM Models
│   │   ├── __init__.py
│   │   ├── user.py             # User model with Role enum
│   │   ├── product.py          # Product model
│   │   └── sale.py             # Sale model with relationships
│   │
│   ├── schemas/                # Pydantic validation schemas
│   │   ├── __init__.py
│   │   ├── user.py             # UserLogin, UserResponse, TokenResponse
│   │   ├── product.py          # ProductCreate, ProductUpdate, ProductResponse
│   │   └── sale.py             # SaleCreate, SaleResponse
│   │
│   ├── crud/                   # Database CRUD operations
│   │   ├── __init__.py
│   │   ├── user.py             # create_user, authenticate_user
│   │   ├── product.py          # get_product, create_product, update, delete
│   │   └── sale.py             # create_sale, get_sales, get_sales_by_product
│   │
│   ├── routes/                 # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py             # POST /auth/login
│   │   ├── products.py         # GET/POST/PUT/DELETE /products
│   │   ├── sales.py            # POST/GET /sales
│   │   ├── dashboard.py        # GET /dashboard/summary
│   │   └── ai.py               # GET /ai/predict, /ai/reorder-suggestion
│   │
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   └── predictor.py        # SalesPredictor class (LinearRegression)
│   │
│   ├── middleware/             # Authentication & authorization
│   │   ├── __init__.py
│   │   └── auth.py             # JWT verification, role checking
│   │
│   └── utils/                  # Helper utilities
│       ├── __init__.py
│       ├── security.py         # JWT creation/verification, password hashing
│       └── seed_data.py        # Database initialization with test data
│
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── test_api.py                # API tests with pytest
├── run.sh                     # Startup script
└── venv/                      # Virtual environment (auto-created)
```

### Frontend Directory Tree

```
frontend/
├── public/                    # Static files
│
├── src/
│   ├── main.jsx              # React entry point
│   ├── App.jsx               # Main app router
│   ├── index.css             # Global Tailwind styles
│   ├── App.css               # App-specific styles
│   │
│   ├── pages/                # Page components (routes)
│   │   ├── Login.jsx         # Authentication page
│   │   ├── Dashboard.jsx     # Summary + AI prediction widget
│   │   └── Inventory.jsx     # Product CRUD + sales recording
│   │
│   ├── components/           # Reusable components
│   │   ├── Header.jsx        # Navigation + user menu
│   │   ├── ProtectedRoute.jsx # Route guard for authenticated pages
│   │   └── ProductModal.jsx  # Product create/edit modal
│   │
│   └── services/             # API communication
│       ├── api.js            # Axios instance with interceptors
│       └── auth.js           # Authentication service (login, logout, token)
│
├── package.json              # npm dependencies
├── vite.config.js           # Vite bundler configuration
├── tailwind.config.js       # Tailwind CSS configuration
├── postcss.config.js        # PostCSS configuration
├── index.html               # HTML template
├── .env.example             # Environment variables template
├── run.sh                   # Startup script
└── node_modules/            # Dependencies (auto-installed)
```

---

## 🔄 Data Flow

### 1. Authentication Flow

```
User Input (Login Page)
    ↓
[Frontend] POST /auth/login {username, password}
    ↓
[Backend] auth.py route receives request
    ↓
[CRUD] authenticate_user() checks database
    ↓
[Security] verify_password() compares bcrypt hashes
    ↓
[JWT] create_access_token() generates JWT
    ↓
[Response] Returns {access_token, user}
    ↓
[Frontend] Stores token in localStorage
    ↓
[Navigation] Redirects to /dashboard
```

### 2. Product CRUD Flow

```
[Admin User] clicks "Create Product"
    ↓
[Frontend] ProductModal.jsx renders form
    ↓
User fills form → clicks Save
    ↓
[Frontend] POST /products {name, category, price, ...}
    ↓
[API Middleware] Verifies JWT token
    ↓
[Middleware] Checks role == "admin"
    ↓
[Route Handler] products.py creates_product_item()
    ↓
[Schema] ProductCreate validates input
    ↓
[CRUD] create_product() saves to database
    ↓
[Response] Returns ProductResponse
    ↓
[Frontend] Updates products list, closes modal
```

### 3. Sales Recording Flow

```
[Staff User] clicks "Record Sale"
    ↓
[Frontend] SaleModal appears with products dropdown
    ↓
User selects product → enters quantity
    ↓
Frontend calculates: total_price = quantity × product.price
    ↓
[Frontend] POST /sales {product_id, quantity_sold, total_price}
    ↓
[Middleware] JWT verified, requires STAFF or ADMIN role
    ↓
[CRUD] create_sale() function:
  ├─ Checks product exists
  ├─ Checks stock >= quantity_sold
  ├─ Creates Sale record
  ├─ Decrements product.stock_quantity
  └─ Commits transaction
    ↓
[Response] Returns SaleResponse with sale data
    ↓
[Frontend] Success message, refreshes products list
```

### 4. AI Prediction Flow

```
[User] Dashboard page loads
    ↓
[Frontend] User selects product → clicks "Predict"
    ↓
[Frontend] GET /ai/predict?product_id=1
    ↓
[Middleware] JWT verified
    ↓
[Route] ai.py predict_sales() handler
    ↓
[Service] SalesPredictor.predict(db, product_id)
    ↓
[CRUD] get_sales_by_product() retrieves last 30 days
    ↓
[ML Logic]
  ├─ If <2 days data: Use fallback (average)
  ├─ Else: Aggregate daily sales
  │   X = [0, 1, 2, 3, ... n]  (day numbers)
  │   y = [5, 7, 4, 6, ... m]  (quantities sold)
  │
  ├─ Train: LinearRegression.fit(X, y)
  │
  ├─ Predict: future_days = [n+1, n+2, ..., n+7]
  │   predictions = model.predict(future_days)
  │
  └─ Ensure no negative values
    ↓
[Response] Returns {method, predictions, total_7days, confidence}
    ↓
[Frontend] Renders chart with predictions
```

---

## 🔐 Security Architecture

### Authentication & Authorization Flow

```
┌─────────────────────────────────────────┐
│  1. USER LOGIN                          │
│  POST /auth/login {username, password}  │
└──────────────┬──────────────────────────┘
               │
        Password Hash Check
               │
┌──────────────▼──────────────────────────┐
│  2. JWT GENERATION                      │
│  payload = {sub: user_id, role: 'admin'}│
│  signed with JWT_SECRET                 │
└──────────────┬──────────────────────────┘
               │
        Return Token to Client
               │
┌──────────────▼──────────────────────────┐
│  3. TOKEN STORAGE                       │
│  localStorage.setItem('token', jwt)     │
└──────────────┬──────────────────────────┘
               │
        Include in API Requests
               │
┌──────────────▼──────────────────────────────────┐
│  4. MIDDLEWARE VERIFICATION                     │
│  get_current_user(token) dependency:            │
│  ├─ Extract token from Authorization header    │
│  ├─ Decode JWT with JWT_SECRET                 │
│  ├─ Verify signature & expiration              │
│  └─ Get user from database                     │
└──────────────┬───────────────────────────────────┘
               │
        Role-Based Access Control
               │
┌──────────────▼──────────────────────────────────┐
│  5. AUTHORIZATION CHECK                        │
│  require_role(Role.ADMIN):                      │
│  ├─ Check user.role == 'admin'                 │
│  ├─ If yes: Execute endpoint                   │
│  └─ If no: Return 403 Forbidden                │
└──────────────────────────────────────────────────┘
```

### Password Security

```
User Input "admin123"
    ↓
[Backend] hash_password(password) using bcrypt
    ↓
Store hashed: $2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5YmMxSUExMgJi
    ↓
[Later] User Login with "admin123"
    ↓
[Backend] verify_password(plain, hashed) using bcrypt
    ↓
Bcrypt compares securely (timing-attack resistant)
    ↓
Return True/False
```

---

## 🤖 AI/ML Architecture

### Sales Predictor Class Structure

```python
SalesPredictor
├── predict(db, product_id, days_history=30)
│   ├── Input: Database session, Product ID
│   ├── Process:
│   │   ├─ Query sales data from last 30 days
│   │   ├─ Aggregate by day (sum quantities)
│   │   ├─ Prepare training data:
│   │   │   X = [[0], [1], [2], ..., [n]]  (day indices)
│   │   │   y = [5, 7, 4, 6, ..., m]       (quantities)
│   │   ├─ Train LinearRegression model
│   │   ├─ Predict next 7 days
│   │   └─ Ensure non-negative predictions
│   └─ Output: {method, predictions, total_7days, confidence}
│
└── get_reorder_suggestion(db, product_id, current_stock, min_limit)
    ├── Input: DB, Product ID, Current Stock, Minimum Limit
    ├── Call: predict() to get 7-day forecast
    ├── Calculate:
    │   required = predicted_total + safety_buffer(20%) - current_stock
    ├── Set urgency:
    │   - "high" if current_stock < min_limit
    │   - "medium" otherwise
    └── Output: {recommendation, quantity, urgency}
```

### Model Training & Prediction Example

```
Historical Data (30 days):
Date          Quantity
2025-12-23    5
2025-12-24    7
2025-12-25    4
2025-12-26    6
...

Training Data:
X = [[0], [1], [2], [3], ...]
y = [5, 7, 4, 6, ...]

LinearRegression learns:
y = slope * X + intercept
Example: y = 0.5X + 4.5

Prediction for next 7 days (X = 30 to 36):
Day 1: 0.5 * 30 + 4.5 = 19.5 → 19
Day 2: 0.5 * 31 + 4.5 = 20.0 → 20
...
Day 7: 0.5 * 36 + 4.5 = 22.5 → 22
```

---

## 🔌 API Endpoint Architecture

### Route Organization

```
Backend Routes
│
├── /auth (AuthRouter)
│   └── POST /login → TokenResponse
│
├── /products (ProductsRouter)
│   ├── GET / → List[ProductResponse]
│   ├── GET /{id} → ProductResponse
│   ├── GET /low-stock → List[ProductResponse]
│   ├── POST / → ProductResponse (Admin)
│   ├── PUT /{id} → ProductResponse (Admin)
│   └── DELETE /{id} → 204 No Content (Admin)
│
├── /sales (SalesRouter)
│   ├── POST / → SaleResponse (Staff/Admin)
│   ├── GET / → List[SaleResponse]
│   └── GET /today → List[SaleResponse]
│
├── /dashboard (DashboardRouter)
│   └── GET /summary → DashboardSummary
│
├── /ai (AIRouter)
│   ├── GET /predict → PredictionResponse
│   └── GET /reorder-suggestion → ReorderSuggestion
│
├── / (Root)
│   └── GET / → AppInfo
│
└── /health (Health Check)
    └── GET / → {status: "ok"}
```

---

## 💾 Database Relationships

### ER Diagram

```
┌──────────────┐
│   USERS      │
├──────────────┤
│ id (PK)      │
│ username (U) │───┐
│ password     │   │
│ role         │   │
└──────────────┘   │
                   │ 1:N
                   │ (staff_id)
                   │
                   ▼
           ┌──────────────┐
           │   SALES      │
           ├──────────────┤
           │ id (PK)      │
           │ product_id   ├──┐
           │ staff_id (FK)│  │
           │ quantity     │  │
           │ sale_date    │  │ N:1
           │ total_price  │  │
           └──────────────┘  │
                             │
                             │
                ┌────────────┘
                │
                ▼
        ┌──────────────┐
        │   PRODUCTS   │
        ├──────────────┤
        │ id (PK)      │
        │ name         │
        │ category     │
        │ price        │
        │ stock_qty    │
        │ min_limit    │
        └──────────────┘
        
Relationships:
- User → Sales (1:N) - One staff records many sales
- Product → Sales (1:N) - One product has many sales
- Sales.product_id FK → Products.id (cascade delete)
- Sales.staff_id FK → Users.id
```

---

## 🚀 Deployment Ready Checklist

- [x] Modular code structure (separation of concerns)
- [x] Configuration management (.env files)
- [x] Database migrations supported (SQLAlchemy)
- [x] Error handling & validation
- [x] CORS configuration for frontend
- [x] JWT token expiration
- [x] Role-based access control
- [x] Input validation (Pydantic)
- [x] API documentation (Swagger/ReDoc)
- [x] Seed data for testing
- [x] Comprehensive README
- [x] Test examples

---

## 📈 Performance Considerations

1. **Database Indexing**: 
   - `users.username` indexed (unique)
   - `sales.sale_date` indexed (date queries)
   - `products.name` indexed (search)

2. **Query Optimization**:
   - Relationships use lazy loading
   - Pagination on list endpoints (skip/limit)
   - Date filtering for sales queries

3. **API Performance**:
   - JWT validation cached in middleware
   - CORS pre-flight optimization
   - Response compression ready

4. **Frontend Performance**:
   - React Router lazy loading ready
   - Tailwind CSS optimized
   - Component-based architecture

---

## 🔄 Scalability Path

For production scaling:

1. **Database**: Migrate from SQLite to PostgreSQL
2. **Authentication**: Use OAuth2 (Google, Microsoft)
3. **Caching**: Implement Redis for session/prediction cache
4. **ML**: Move predictor to separate microservice
5. **Frontend**: Add state management (Redux/Zustand)
6. **Monitoring**: Add logging (Sentry/DataDog)
7. **API**: Rate limiting & request throttling
8. **Deployment**: Docker containerization + Kubernetes

---

**Version**: 1.0.0 MVP  
**Architecture Type**: Three-tier (Frontend-Backend-Database)  
**Design Pattern**: MVC + Service Layer
