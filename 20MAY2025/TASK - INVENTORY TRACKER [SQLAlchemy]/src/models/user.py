from typing import Literal, Optional 
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Float, String, Boolean, TIMESTAMP, func
from sqlalchemy import Column
from sqlalchemy.orm import relationship

from src.models.base import Base


class User(Base):
    
    __tablename__ = 'users'
    
    user_id: int = Column(Integer, primary_key=True)
    username: str = Column(String[50], nullable=False, unique=True)
    password: str = Column(String[100], nullable=False)
    email: str = Column(String(100), nullable=False, unique=True)
    is_active: bool = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    permissions = relationship(
        'Permission',
        secondary='user_permissions',
        back_populates='users'
    )
    