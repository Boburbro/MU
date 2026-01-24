from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.middleware.auth import get_current_user
from app.crud.product import get_product
from app.services.predictor import SalesPredictor

router = APIRouter(prefix="/ai", tags=["ai-predictions"])

@router.get("/predict")
async def predict_sales(
    product_id: int = Query(..., gt=0),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get 7-day sales prediction for product"""
    
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    prediction = SalesPredictor.predict(db, product_id)
    
    return {
        "product_id": product_id,
        "product_name": product.name,
        "current_stock": product.stock_quantity,
        "prediction": prediction
    }

@router.get("/reorder-suggestion")
async def get_reorder_suggestion(
    product_id: int = Query(..., gt=0),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get reorder suggestion based on prediction"""
    
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    suggestion = SalesPredictor.get_reorder_suggestion(
        db,
        product_id,
        product.stock_quantity,
        product.min_limit
    )
    
    return {
        "product_id": product_id,
        "product_name": product.name,
        **suggestion
    }
