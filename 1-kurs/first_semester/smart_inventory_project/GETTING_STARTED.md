# 🚀 Getting Started Guide

Fastest way to run Smart Inventory system locally.

## 📋 Prerequisites

- **Python** 3.8+ ([download](https://www.python.org/downloads/))
- **Node.js** 16+ ([download](https://nodejs.org/))
- **Git** (optional, for cloning)

## ⚡ Quick Start (5 minutes)

### Option 1: Automated Installation (Linux/Mac)

```bash
chmod +x install.sh
./install.sh
```

Then run in two terminals:
```bash
# Terminal 1
cd backend
./venv/bin/python -m uvicorn app.main:app --reload

# Terminal 2
cd frontend
npm run dev
```

### Option 2: Manual Installation

#### Step 1: Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate venv (Linux/Mac)
source venv/bin/activate
# OR on Windows
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run backend
python -m uvicorn app.main:app --reload
```

✅ Backend should be running at **http://localhost:8000**

#### Step 2: Frontend Setup (new terminal)

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.example .env

# Run frontend
npm run dev
```

✅ Frontend should be running at **http://localhost:5173**

## 🔐 Test the System

### 1. Open in Browser
- Go to http://localhost:5173

### 2. Login with Test Credentials
```
Admin:
  Username: admin
  Password: admin123

Staff:
  Username: staff
  Password: staff123
```

### 3. Explore Features

**Admin User Can:**
- ✅ View Dashboard with statistics
- ✅ Create, Edit, Delete Products
- ✅ Record Sales
- ✅ View Predictions
- ✅ See Low Stock Alerts

**Staff User Can:**
- ✅ View Dashboard
- ✅ View Products (read-only)
- ✅ Record Sales
- ✅ View Predictions
- ✅ See Low Stock Alerts

## 🧪 Test API Endpoints

Copy-paste these commands in terminal after backend is running:

### Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

**Save the `access_token` from response** to use in other requests.

### Get All Products
```bash
curl -X GET http://localhost:8000/products \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### View API Documentation
Visit: http://localhost:8000/docs

## 📱 Frontend Features to Try

1. **Dashboard** - See statistics and predictions
   - Total products count
   - Low stock alerts
   - Today's revenue
   - 7-day AI prediction widget

2. **Inventory** - Manage products
   - View all products in table
   - Create new product (Admin)
   - Edit product (Admin)
   - Delete product (Admin)
   - Record sales

3. **AI Prediction** - Sales forecasting
   - Select a product
   - Click "Predict"
   - See 7-day forecast chart

## 🐛 Troubleshooting

### Backend won't start

**Error: "Address already in use"**
```bash
# Kill process on port 8000
lsof -i :8000
kill -9 <PID>
```

**Error: "Module not found"**
```bash
# Make sure venv is activated
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows

# Reinstall packages
pip install -r requirements.txt
```

### Frontend won't start

**Error: "npm: command not found"**
- Install Node.js from https://nodejs.org/

**Error: "Port 5173 already in use"**
```bash
# Kill process on port 5173
lsof -i :5173
kill -9 <PID>
```

### Database errors

**SQLite database locked**
```bash
# Delete old database
rm backend/smart_inventory.db
# Restart backend (will auto-create)
```

### CORS errors in browser console

**Error: "Access to XMLHttpRequest blocked by CORS"**
1. Make sure backend is running on http://localhost:8000
2. Check `VITE_API_URL` in `frontend/.env`
3. Restart frontend dev server

## 📊 Sample Data

The database is auto-seeded with:

**Users:**
- admin / admin123 (Admin role)
- staff / staff123 (Staff role)

**Products:**
- Coca-Cola (Beverage) - $2.50, 50 stock
- Non/Water (Beverage) - $1.00, 100 stock
- Yog'/Yogurt (Dairy) - $3.50, 20 stock
- Bread (Bakery) - $1.50, 40 stock
- Milk (Dairy) - $2.00, 30 stock

**Sales:**
- Auto-generated sales for last 10 days (for AI prediction testing)

## 🔧 Configuration

### Backend Environment Variables (`backend/.env`)

```env
# Database (SQLite)
DATABASE_URL=sqlite:///./smart_inventory.db

# JWT Configuration
JWT_SECRET=your-super-secret-jwt-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# Flask Configuration
DEBUG=True
```

### Frontend Environment Variables (`frontend/.env`)

```env
# API URL (backend location)
VITE_API_URL=http://localhost:8000
```

## 📚 API Endpoints Quick Reference

```
Authentication
  POST   /auth/login

Products
  GET    /products
  GET    /products/{id}
  GET    /products/low-stock
  POST   /products (Admin)
  PUT    /products/{id} (Admin)
  DELETE /products/{id} (Admin)

Sales
  POST   /sales
  GET    /sales
  GET    /sales/today

Dashboard
  GET    /dashboard/summary

AI Predictions
  GET    /ai/predict?product_id=ID
  GET    /ai/reorder-suggestion?product_id=ID

Utilities
  GET    / (app info)
  GET    /health (health check)
  GET    /docs (Swagger UI)
  GET    /redoc (ReDoc UI)
```

## 🎓 Learning Resources

**Frontend Tech:**
- React Docs: https://react.dev/
- React Router: https://reactrouter.com/
- Tailwind CSS: https://tailwindcss.com/
- Axios: https://axios-http.com/

**Backend Tech:**
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- Pydantic: https://docs.pydantic.dev/

**AI/ML:**
- scikit-learn: https://scikit-learn.org/
- LinearRegression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

## 📞 Support

For issues or questions:
1. Check the [README.md](./README.md) for detailed documentation
2. Review [ARCHITECTURE.md](./ARCHITECTURE.md) for system design
3. Check API docs at http://localhost:8000/docs
4. Look at code comments in the source files

## ✅ Verification Checklist

After starting the system:

- [ ] Backend running on http://localhost:8000
- [ ] Frontend running on http://localhost:5173
- [ ] Can login with admin/admin123
- [ ] Dashboard displays statistics
- [ ] Can view products table
- [ ] Can record a sale
- [ ] AI prediction works
- [ ] API docs visible at http://localhost:8000/docs

---

**Congratulations! 🎉 Smart Inventory is now running!**

Next steps:
- Explore the Dashboard
- Try creating/editing products
- Record some sales
- Check the AI predictions
- Review the code structure
