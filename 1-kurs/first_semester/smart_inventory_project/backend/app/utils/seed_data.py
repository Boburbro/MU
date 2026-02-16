from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.models import User, Product, Sale, Role
from app.utils.security import hash_password
from datetime import datetime, timedelta
import random

def seed_database():
    """Seed database with initial data"""
    db = SessionLocal()
    try:
        # Check if already seeded
        if db.query(User).filter(User.username == "admin").first():
            return
        
        # Create tables
        Base.metadata.create_all(bind=engine)
        
        # Create users
        admin_user = User(
            username="admin",
            password_hashed=hash_password("admin123"),
            role=Role.ADMIN
        )
        staff_user = User(
            username="staff",
            password_hashed=hash_password("staff123"),
            role=Role.STAFF
        )
        db.add(admin_user)
        db.add(staff_user)
        db.commit()
        db.refresh(admin_user)
        db.refresh(staff_user)
        
        # Create products
        products_data = [
            Product(name="Coca-Cola", category="Beverage", price=2.5, stock_quantity=50, min_limit=10),
            Product(name="Non (Water)", category="Beverage", price=1.0, stock_quantity=100, min_limit=20),
            Product(name="Yog' (Yogurt)", category="Dairy", price=3.5, stock_quantity=20, min_limit=5),
            Product(name="Bread", category="Bakery", price=1.5, stock_quantity=40, min_limit=15),
            Product(name="Milk", category="Dairy", price=2.0, stock_quantity=30, min_limit=10),
        ]
        db.add_all(products_data)
        db.commit()
        db.refresh(admin_user)
        db.refresh(staff_user)
        for p in products_data:
            db.refresh(p)
        
        # Create sales for last 10 days
        base_date = datetime.utcnow() - timedelta(days=10)
        for product in products_data:
            for day_offset in range(10):
                sale_date = base_date + timedelta(days=day_offset)
                
                # 1-3 sales per product per day
                for _ in range(random.randint(1, 3)):
                    qty = random.randint(1, 10)
                    total = qty * product.price
                    
                    sale = Sale(
                        product_id=product.id,
                        staff_id=staff_user.id,
                        quantity_sold=qty,
                        sale_date=sale_date,
                        total_price=total
                    )
                    db.add(sale)
        
        db.commit()
        print("✅ Database seeded successfully")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()
