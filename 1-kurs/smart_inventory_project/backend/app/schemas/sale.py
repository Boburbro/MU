from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SaleCreate(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity_sold: int = Field(..., gt=0)
    total_price: float = Field(..., ge=0)

class SaleResponse(BaseModel):
    id: int
    product_id: int
    staff_id: int
    quantity_sold: int
    sale_date: datetime
    total_price: float
    
    class Config:
        from_attributes = True

class SaleWithProduct(SaleResponse):
    product_name: str = ""
