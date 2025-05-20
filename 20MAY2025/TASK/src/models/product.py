from sqlalchemy import create_engine
from sqlalchemy import Integer, Float, String, Column, Table
from sqlalchemy import TIMESTAMP, DateTime, func
from src.models.base import Base

class Product(Base):
    
    __tablename__ = 'products'
    
    product_id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    price: float = Column(Float, nullable=False)
    category: str = Column(String)
    created_at = Column(TIMESTAMP, server_default = func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default = func.current_timestamp(), onupdate=func.current_timestamp())

    def __repr__(self) -> str:
        return f"""Product(product_id={self.product_id}, name={self.name}, price={self.price}, category={self.category}, created_at={self.created_at}, updated_at={self.updated_at})"""
        




    