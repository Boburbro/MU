from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class Role(str, enum.Enum):
    ADMIN = "admin"
    STAFF = "staff"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password_hashed = Column(String(255), nullable=False)
    role = Column(Enum(Role), default=Role.STAFF, nullable=False)
    
    # Relationships
    sales = relationship("Sale", back_populates="staff")
    
    def __repr__(self):
        return f"<User {self.username} ({self.role})>"
