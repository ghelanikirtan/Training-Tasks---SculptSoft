from src.constants import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Modulees import 
from src.models.base import Base
from src.models.product import Product
from src.models.warehouse import Warehouse
from src.models.inventory import Inventory
from src.models.transaction import Transaction


class DatabaseService:
    
    
    def __init__(self):
        
        self.engine = create_engine(URL)
        self.Session = sessionmaker(bind=self.engine)
        self.conn = self.engine.connect()
        self.session = self.Session()
        
    def make_migrations(self):
        Base.metadata.create_all(self.engine)
        # pass
        
    def add_warehouse(self, warehouse:Warehouse):
        self.session.add(warehouse)
        self.session.commit()
        

        
        
        