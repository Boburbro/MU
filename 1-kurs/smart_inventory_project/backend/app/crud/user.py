from sqlalchemy.orm import Session
from app.models import User
from app.utils.security import hash_password, verify_password

def get_user_by_username(db: Session, username: str):
    """Get user by username"""
    return db.query(User).filter(User.username == username).first()

def get_user_by_id(db: Session, user_id: int):
    """Get user by ID"""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, username: str, password: str, role: str = "staff"):
    """Create new user"""
    hashed_password = hash_password(password)
    user = User(username=username, password_hashed=hashed_password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    """Authenticate user"""
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.password_hashed):
        return None
    return user
