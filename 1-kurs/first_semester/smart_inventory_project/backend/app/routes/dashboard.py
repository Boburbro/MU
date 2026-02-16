from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.middleware.auth import get_current_user
from app.crud.product import get_low_stock_products, get_products
from app.crud.sale import get_today_sales

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/summary")
async def get_dashboard_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get dashboard summary (statistics)"""
    
    # Get low stock products
    low_stock = get_low_stock_products(db)
    
    # Get today's sales
    today_sales = get_today_sales(db)
    
    # Calculate statistics
    total_products = len(get_products(db, skip=0, limit=1000))
    total_today_sales = sum(s.total_price for s in today_sales)
    total_today_quantity = sum(s.quantity_sold for s in today_sales)
    
    return {
        "total_products": total_products,
        "low_stock_count": len(low_stock),
        "low_stock_products": [
            {
                "id": p.id,
                "name": p.name,
                "stock": p.stock_quantity,
                "min_limit": p.min_limit
            }
            for p in low_stock[:5]  # Top 5
        ],
        "today_sales": {
            "count": len(today_sales),
            "total_quantity": total_today_quantity,
            "total_revenue": round(total_today_sales, 2)
        }
    }
