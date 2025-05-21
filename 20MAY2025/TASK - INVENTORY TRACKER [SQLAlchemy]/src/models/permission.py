from typing import Literal, Optional
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Integer, Float, String, TIMESTAMP, func
from sqlalchemy import Column, Table
from sqlalchemy.orm import relationship
from src.models.base import Base


user_permissions = Table(
    'user_permissions',
    Base.metadata,
    
    Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.permission_id'), primary_key=True),
    Column('granted_at', TIMESTAMP, server_default=func.current_timestamp())
    
)


class Permission(Base):
    
    __tablename__ = "permissions"

    permission_id = Column(Integer, primary_key=True)
    resource: Literal['warehouse', 'inventory', 'transaction', 'product'] = Column(String(20), nullable=False)
    action: Literal['read', 'write'] = Column(String(15), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    users = relationship(
        'User',
        secondary="user_permissions",
        back_populates='permissions'
    )
