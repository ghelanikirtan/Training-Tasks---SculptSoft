from typing import Optional, List
from datetime import datetime
from src.models.inventory import Inventory
from src.services.database import DatabaseService
from src.services.queries import *

class InventoryService(DatabaseService):
    def __init__(self):
        super().__init__()

    def add_inventory(self, inventory: Inventory) -> int:
        """Add inventory record."""
        inventory_details = (
            inventory.product_id,
            inventory.warehouse_id,
            inventory.quantity,
            inventory.last_restock_date or datetime.now()
        )
        
        try:
            self.cursor.execute(ADD_INVENTORY, inventory_details)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"An error occurred while adding inventory: {e}")
            return None
            
    def get_inventory(self, product_id: int, warehouse_id: int) -> Optional[Inventory]:
        """Get inventory for a specific product in a specific warehouse."""
        try:
            query = """
            SELECT inventory_id, product_id, warehouse_id, quantity, last_restock_date, created_at, updated_at 
            FROM inventory
            WHERE product_id = ? AND warehouse_id = ?
            """
            
            self.cursor.execute(query, (product_id, warehouse_id))
            row = self.cursor.fetchone()
            
            if row:
                return Inventory(
                    inventory_id=row[0],
                    product_id=row[1],
                    warehouse_id=row[2],
                    quantity=row[3],
                    last_restock_date=row[4],
                    created_at=row[5],
                    updated_at=row[6]
                )
            return None
        except Exception as e:
            print(f"An error occurred [get_inventory]: {e}")
            return None
        
    def get_all_inventory(self) -> List[Inventory]:
        """Get all inventory records."""
        try:
            query = """
            SELECT inventory_id, product_id, warehouse_id, quantity, last_restock_date, created_at, updated_at 
            FROM inventory
            """
            
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            inventory_list = []
            
            for row in records:
                inventory_list.append(Inventory(
                    inventory_id=row[0],
                    product_id=row[1],
                    warehouse_id=row[2],
                    quantity=row[3],
                    last_restock_date=row[4],
                    created_at=row[5],
                    updated_at=row[6]
                ))
            
            return inventory_list
        except Exception as e:
            print(f"An error occurred [get_all_inventory]: {e}")
            return []
            
    def update_inventory(self, inventory: Inventory) -> bool:
        """Update inventory quantity."""
        try:
            inventory_details = (
                inventory.quantity,
                inventory.last_restock_date or datetime.now(),
                inventory.product_id,
                inventory.warehouse_id
            )
            
            self.cursor.execute(UPDATE_INVENTORY, inventory_details)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [update_inventory]: {e}")
            return False
            
    def delete_inventory(self, inventory_id: int) -> bool:
        """Delete an inventory record."""
        try:
            self.cursor.execute(DELETE_INVENTORY, (inventory_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [delete_inventory]: {e}")
            return False