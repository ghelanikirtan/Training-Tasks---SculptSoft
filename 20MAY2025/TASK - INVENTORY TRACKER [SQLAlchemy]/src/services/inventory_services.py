from typing import List, Optional
from sqlalchemy import select, update, delete
from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.inventory import Inventory
from src.services.database import DatabaseService




class InventoryService:
    
    def __init__(self, services: DatabaseService = None):
        self.services = services if services else DatabaseService()
        self.engine = self.services.engine
        self.conn = self.services.conn
        self.session = self.services.session

    def add_inventory(self, inventory_item: Inventory, session:Session):
        session.add(inventory_item)
        session.flush()
        
    def update_inventory(self, inventory_item: Inventory, session:Session):
        
        q = update(Inventory
                   ).where(and_(Inventory.product_id == inventory_item.product_id, Inventory.warehouse_id == inventory_item.warehouse_id)
            ).values(quantity = inventory_item.quantity)
        session.execute(q)           
        session.flush()

    def get_inventory(self, product_id: int , warehouse_id: int, session:Session) -> Optional[Inventory]:
        try:
            
            q = select(Inventory).where(
                and_(Inventory.product_id == product_id, 
                     Inventory.warehouse_id == warehouse_id
                     ))
            inventory: Inventory = session.execute(q).scalars().first()
            return inventory
        
        except SQLAlchemyError as e:
            print(f"Inventory Item Fetching failed: {e}")
            return None
