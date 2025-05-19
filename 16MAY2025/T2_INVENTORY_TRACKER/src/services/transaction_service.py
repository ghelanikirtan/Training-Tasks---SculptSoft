from typing import Optional, List
from src.models.transaction import Transaction
from src.models.inventory import Inventory
from src.services.database import DatabaseService
from src.services.inventory_service import InventoryService
from src.services.queries import *

class TransactionService:
    def __init__(self, services: DatabaseService = None):
        self.services = DatabaseService()
        self.inventory_service = InventoryService(services=self.services)
        self.services.make_migrations()
        self.cursor = self.services.cursor
        self.connection = self.services.connection

    def add_transaction(self, transaction: Transaction) -> int:
        """Add a transaction and update inventory."""
        transaction_details = (
            transaction.product_id,
            transaction.warehouse_id,
            transaction.quantity,
            transaction.transaction_type,
        )
        
        try:
            self.connection.execute("BEGIN TRANSACTION")
            
            self.cursor.execute(ADD_TRANSACTION, transaction_details)
            
            # Update inventory 
            inventory = self.inventory_service.get_inventory(
                transaction.product_id, 
                transaction.warehouse_id
            )
            
            if inventory:
                if transaction.transaction_type == 'in':
                    inventory.quantity += transaction.quantity
                elif transaction.transaction_type == 'out':
                    inventory.quantity -= transaction.quantity
                    if inventory.quantity < 0:
                        raise ValueError("Insufficient inventory")
                self.inventory_service.update_inventory(inventory)
            else:
                # Create new inventory record if it doesn't exist and transaction is 'in'
                if transaction.transaction_type == 'in':
                    new_inventory = Inventory(
                        product_id=transaction.product_id,
                        warehouse_id=transaction.warehouse_id,
                        quantity=transaction.quantity
                    )
                    self.inventory_service.add_inventory(new_inventory)
                else:
                    raise ValueError("Cannot perform transaction on non-existent inventory")
            
            # Commit the transaction
            self.connection.commit()
            return transaction.transaction_id
        except Exception as e:
            # Rollback in case of error
            self.connection.rollback()
            print(f"An error occurred while adding transaction: {e}")
            return None
            
    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]:
        """Get a transaction by its ID."""
        try:
            query = f"""
            SELECT transaction_id, product_id, warehouse_id, quantity, transaction_type, transaction_date
            FROM transactions
            WHERE transaction_id = {transaction_id}
            """
            
            records = self.cursor.execute(query).fetchall()
            transaction: Transaction = None
            for row in records:
                transaction = Transaction(
                    transaction_id=row[0],
                    product_id=row[1],
                    warehouse_id=row[2],
                    quantity=row[3],
                    transaction_type=row[4],
                    transaction_date=row[5]
                )
            return transaction
        except Exception as e:
            print(f"An error occurred [get_transaction_by_id]: {e}")
            return None
        
    def get_transactions_by_product(self, product_id: int) -> List[Transaction]:
        """Get all transactions for a specific product."""
        try:
            query = f"""
            SELECT transaction_id, product_id, warehouse_id, quantity, transaction_type, transaction_date
            FROM transactions
            WHERE product_id = {product_id}
            ORDER BY transaction_date DESC;
            """
            
            records = self.cursor.execute(query).fetchall()
            transactions : List[Transaction] = []
            
            for row in records:
                transactions.append(
                    Transaction(
                        transaction_id=row[0],
                        product_id=row[1],
                        warehouse_id=row[2],
                        quantity=row[3],
                        transaction_type=row[4],
                        transaction_date=row[5]
                ))
            
            return transactions
        except Exception as e:
            print(f"An error occurred [get_transactions_by_product]: {e}")
            return []