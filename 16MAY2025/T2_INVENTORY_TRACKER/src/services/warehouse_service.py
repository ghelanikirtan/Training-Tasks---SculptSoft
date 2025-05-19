from typing import Optional, List
from src.models.warehouse import Warehouse
from src.services.database import DatabaseService
from src.services.queries import *

class WarehouseService:
    def __init__(self, services: DatabaseService = None):
        self.services = DatabaseService()
        self.services.make_migrations()
        self.cursor = self.services.cursor
        self.connection = self.services.connection

    def add_warehouse(self, warehouse: Warehouse):
        """Add a warehouse to the warehouses table."""
        warehouse_details = (
            warehouse.name,
            warehouse.location,
            warehouse.capacity,
            warehouse.status
        )
        
        try:
            self.cursor.execute(ADD_WAREHOUSE, warehouse_details)
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred while adding warehouse: {e}")
            
    def get_warehouse_by_id(self, warehouse_id: int) -> Optional[Warehouse]:
        """Get a warehouse by its ID."""
        try:
            query = f"""
            SELECT warehouse_id, name, location, capacity, status, created_at, updated_at 
            FROM warehouses
            WHERE warehouse_id = {warehouse_id};
            """
            
            records = self.cursor.execute(query).fetchall()
            warehouse: Warehouse = None
            for row in records:
                warehouse = Warehouse(
                    warehouse_id=row[0],
                    name=row[1],
                    location=row[2],
                    capacity=row[3],
                    status=row[4],
                    created_at=row[5],
                    updated_at=row[6]
                )
            return warehouse
        except Exception as e:
            print(f"An error occurred [get_warehouse_by_id]: {e}")
            return None
        
    def get_all_warehouses(self) -> List[Warehouse]:
        """Get all warehouses."""
        try:
            query = """
            SELECT warehouse_id, name, location, capacity, status, created_at, updated_at 
            FROM warehouses;
            """
            
            records = self.cursor.execute(query).fetchall()
            warehouses : List[Warehouse] = []
            for row in records:
                warehouses.append(
                    Warehouse(
                        warehouse_id=row[0],
                        name=row[1],
                        location=row[2],
                        capacity=row[3],
                        status=row[4],
                        created_at=row[5],
                        updated_at=row[6]
                    )
                )
            
            return warehouses
        except Exception as e:
            print(f"An error occurred [get_all_warehouses]: {e}")
            return []
            
    def update_warehouse(self, warehouse: Warehouse) -> bool:
        """Update a warehouse."""
        pass
        # try:
        #     warehouse_details = (
        #         warehouse.name,
        #         warehouse.location,
        #         warehouse.capacity,
        #         warehouse.status,
        #         warehouse.warehouse_id
        #     )
            
        #     self.cursor.execute(UPDATE_WAREHOUSE, warehouse_details)
        #     self.connection.commit()
        #     return True
        # except Exception as e:
        #     print(f"An error occurred [update_warehouse]: {e}")
        #     return False
            
    def delete_warehouse(self, warehouse_id: int) -> bool:
        """Delete a warehouse."""
        try:
            query = f"""
            DELETE FROM warehouses
            WHERE warehouse_id = {warehouse_id};
            """
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [delete_warehouse]: {e}")
            return False