from typing import Literal
from sqlalchemy import Integer, Float, String, Column
from sqlalchemy import ForeignKey, TIMESTAMP, func

from src.models.base import Base


class Transaction(Base):
    
    __tablename__ = "transactions"

    transaction_id: int = Column(Integer, primary_key=True, autoincrement=True)
    product_id: int = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    warehouse_id: int = Column(Integer, ForeignKey('warehouses.warehouse_id'), nullable=False)
    quantity: int = Column(Integer, nullable=False)
    transaction_type: Literal['in', 'out', 'transfer'] = Column(String(10), nullable=False)
    transaction_date: TIMESTAMP = Column(TIMESTAMP, server_default = func.current_timestamp())

    def __repr__(self) -> str:
        return f"""Transaction(transaction_id={self.transaction_id},product_id={self.product_id}, warehouse_id={self.warehouse_id}, quantity={self.quantity}, transaction_type={self.transaction_type}, transaction_date={self.transaction_date})"""
    
    