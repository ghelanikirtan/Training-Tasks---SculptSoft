from typing import Literal
from sqlalchemy import Integer, Float, String, Column, Table
from sqlalchemy import TIMESTAMP, func
from src.models.base import Base 


class Warehouse(Base):
    
    __tablename__ = 'warehouses'
    
    warehouse_id:int = Column(Integer, primary_key = True, autoincrement=True)
    name: str = Column(String, nullable=False)
    location: str = Column(String, nullable=False)
    capacity: int = Column(Integer)
    status: Literal['active', 'inactive', 'maintenance']= Column(String, default='active')
    created_at = Column(TIMESTAMP, server_default = func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default = func.current_timestamp(), onupdate=func.current_timestamp())

    def __repr__(self) -> str:
        return f"""Warehouse(warehouse_id={self.warehouse_id}, name={self.name}, location={self.location}, capacity={self.capacity}, status={self.status}, created_at={self.created_at}, updated_at={self.updated_at})"""