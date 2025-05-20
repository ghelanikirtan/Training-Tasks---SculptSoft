
from typing import List, Optional
from sqlalchemy import select, update, delete
from src.models.product import Product
from src.services.database import DatabaseService



class ProductService:
    
    def __init__(self, services: DatabaseService = None):

        self.services = services if services else DatabaseService()
        self.engine = self.services.engine
        self.conn = self.services.conn
        self.session = self.services.session
        
    def add_product(self, product:Product):
        session = self.services.Session()
        session.add(product)
        session.commit()
        session.close()
        del session
        
    def get_product_by_id(self, product_id: int) -> Product:
        session = self.services.Session()
        query = select(Product).where(Product.product_id == product_id)
        product: Product= session.execute(query).scalars().first()
        session.commit()
        session.close()
        del session
        return product
    
    def get_all_products(self) -> List[Product]:
        # session = self.services.Session()
        query = select(Product)
        products: List[Product] = self.session.execute(query).scalars().all()
        # session.commit()
        # session.close()
        # del session
        return products
    
    
    
    