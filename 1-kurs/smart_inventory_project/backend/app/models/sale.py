from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    staff_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    sale_date = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    total_price = Column(Float, nullable=False)
    
    # Relationships
    product = relationship("Product", back_populates="sales")
    staff = relationship("User", back_populates="sales")
    
    def __repr__(self):
        return f"<Sale product_id={self.product_id} qty={self.quantity_sold} on {self.sale_date}>"
