from typing import Literal 
from sqlalchemy import TIMESTAMP, ForeignKey, Integer, Float, String, DateTime, Column
from sqlalchemy import func

from src.models.base import Base



class Inventory(Base):
    
    __tablename__ = 'inventory'

    inventory_id: int = Column(Integer, primary_key=True)
    product_id: int = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    warehouse_id: int = Column(Integer, ForeignKey('warehouses.warehouse_id'), nullable=False)
    quantity: int = Column(Integer, nullable=False)
    last_restock_date = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    created_at = Column(TIMESTAMP, server_default = func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default = func.current_timestamp(), onupdate=func.current_timestamp())

    def __repr__(self) -> str:
        return f"""Inventory(inventory_id={self.inventory_id}, product_id={self.product_id}, warehouse_id={self.warehouse_id}, quantity={self.quantity}, last_restock_date={self.last_restock_date}, created_at={self.created_at}, updated_at={self.updated_at})"""

    


