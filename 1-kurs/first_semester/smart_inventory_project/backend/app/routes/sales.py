from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, Role
from app.middleware.auth import get_current_user, require_role
from app.schemas.sale import SaleCreate, SaleResponse
from app.crud.sale import create_sale, get_sales, get_today_sales

router = APIRouter(prefix="/sales", tags=["sales"])

@router.post("", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
async def record_sale(
    sale: SaleCreate,
    current_user: User = Depends(require_role(Role.STAFF, Role.ADMIN)),
    db: Session = Depends(get_db)
):
    """Record new sale (Staff & Admin)"""
    created_sale = create_sale(db, sale, current_user.id)
    if not created_sale:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid product or insufficient stock"
        )
    return created_sale

@router.get("", response_model=list[SaleResponse])
async def list_sales(
    days: int = Query(30, ge=1, le=365),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get sales history"""
    return get_sales(db, days=days, skip=skip, limit=limit)

@router.get("/today", response_model=list[SaleResponse])
async def get_today_sales_list(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get today's sales"""
    return get_today_sales(db)
