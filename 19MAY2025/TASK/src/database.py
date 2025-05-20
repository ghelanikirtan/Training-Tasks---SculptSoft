from src.constants import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Modulees import 
from src.models.base import Base
from src.models.products import Product
from src.models.warehouse import Warehouse


class DatabaseService:
    
    
    def __init__(self):
        
        self.engine = create_engine(URL)
        self.conn = self.engine.connect()
        self.product: Product = Product()
        self.warehouse: Warehouse = Warehouse()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
    def make_migrations(self):
        Base.metadata.create_all(self.engine)
        # pass
        
        
    def add_product(self, product:Product):
        self.session.add(product)
        self.session.commit()
        
    def add_warehouse(self, warehouse:Warehouse):
        self.session.add(warehouse)
        self.session.commit()
        
        