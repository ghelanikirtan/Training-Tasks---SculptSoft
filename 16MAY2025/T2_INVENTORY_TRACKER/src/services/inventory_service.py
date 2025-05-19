from typing import Optional, List
from datetime import datetime
from src.models.inventory import Inventory
from src.services.database import DatabaseService
from src.services.queries import *

class InventoryService:
    def __init__(self, services: DatabaseService = None):
        self.services = DatabaseService()
        self.services.make_migrations()
        self.cursor = self.services.cursor
        self.connection = self.services.connection

    def add_inventory(self, inventory: Inventory):
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
        except Exception as e:
            print(f"An error occurred while adding inventory: {e}")
        else:
            print(f"Inventory p_id: {inventory.product_id} & w_id: {inventory.warehouse_id} of {inventory.quantity} Units added Successfully!")
        
    def get_inventory(self, product_id: int, warehouse_id: int) -> Optional[Inventory]:
        """Get inventory for a specific product in a specific warehouse."""
        try:
            query = f"""
            SELECT inventory_id, product_id, warehouse_id, quantity, last_restock_date, created_at, updated_at 
            FROM inventory
            WHERE product_id = {product_id} AND warehouse_id = {warehouse_id};
            """
            
            records = self.cursor.execute(query).fetchall()
            inventory: Inventory = None 
            for row in records:
                inventory = Inventory(
                    inventory_id=row[0],
                    product_id=row[1],
                    warehouse_id=row[2],
                    quantity=row[3],
                    last_restock_date=row[4],
                    created_at=row[5],
                    updated_at=row[6]
                )
            return inventory
        except Exception as e:
            print(f"An error occurred [get_inventory]: {e}")
            return None
        
    def get_all_inventory(self) -> List[Inventory]:
        """Get all inventory records."""
        try:
            query = f"""
            SELECT inventory_id, product_id, warehouse_id, quantity, last_restock_date, created_at, updated_at 
            FROM inventory;
            """
            
            records = self.cursor.execute(query).fetchall()
            inventory_list: List[Inventory] = []
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
            # inventory_details = (
            #     inventory.quantity,
            #     inventory.last_restock_date or datetime.now(),
            #     inventory.product_id,
            #     inventory.warehouse_id
            # )
            
            query = f"""
            UPDATE inventory
            SET quantity = {inventory.quantity}, last_restock_date = {inventory.last_restock_date}, updated_at = CURRENT_TIMESTAMP
            WHERE product_id = {inventory.product_id} AND warehouse_id = {inventory.warehouse_id};
            """
            # self.cursor.execute(UPDATE_INVENTORY, inventory_details)
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [update_inventory]: {e}")
            return False
            
    def delete_inventory(self, inventory_id: int) -> bool:
        """Delete an inventory record."""
        try:
            query = f"""
            DELETE FROM inventory
            WHERE inventory_id = {inventory_id}"""
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [delete_inventory]: {e}")
            return False