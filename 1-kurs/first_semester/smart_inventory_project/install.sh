#!/bin/bash
set -e

echo "🚀 Smart Inventory System - Backend Installation"
echo "================================================"

# Backend setup
echo ""
echo "📦 Setting up Backend..."
cd backend

# Create venv
python3 -m venv venv

# Install packages
./venv/bin/pip install --upgrade pip setuptools wheel > /dev/null 2>&1
./venv/bin/pip install -r requirements.txt > /dev/null 2>&1

# Copy env file
cp .env.example .env

echo "✅ Backend installed successfully"
echo "   Start with: cd backend && ./venv/bin/python -m uvicorn app.main:app --reload"

# Frontend setup
echo ""
echo "📦 Setting up Frontend..."
cd ../frontend

# Install packages
npm install > /dev/null 2>&1

# Copy env file
cp .env.example .env

echo "✅ Frontend installed successfully"
echo "   Start with: cd frontend && npm run dev"

echo ""
echo "🎉 Installation complete!"
echo ""
echo "📋 To run the system:"
echo "   Terminal 1: cd backend && ./venv/bin/python -m uvicorn app.main:app --reload"
echo "   Terminal 2: cd frontend && npm run dev"
echo ""
echo "🔐 Test Credentials:"
echo "   Admin: admin / admin123"
echo "   Staff: staff / staff123"
