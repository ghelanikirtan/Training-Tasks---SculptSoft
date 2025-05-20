from typing import List, Optional
from sqlalchemy import select, update, delete
from src.models.product import Product
from src.models.warehouse import Warehouse
from src.services.database import DatabaseService



class WarehouseService:
    
    def __init__(self, services: DatabaseService = None):

        self.services = services if services else DatabaseService()
        self.engine = self.services.engine
        self.conn = self.services.conn
        self.session = self.services.session
        
    def add_warehouse(self, warehouse:Warehouse):
        session = self.services.Session()
        session.add(warehouse)
        session.commit()
        session.close()
        del session
        
    def get_product_by_id(self, warehouse_id: int) -> Warehouse:
        session = self.services.Session()
        query = select(Warehouse).where(Warehouse.warehouse_id == warehouse_id)
        warehouse: Warehouse = session.execute(query).scalars().first()
        session.commit()
        session.close()
        del session
        return warehouse
    
    def get_all_warehouses(self) -> List[Warehouse]:
        # session = self.services.Session()
        query = select(Warehouse)
        warehouses: List[Warehouse] = self.session.execute(query).scalars().all()
        # session.commit()
        # session.close()
        # del session
        return warehouses
    
    
    
    