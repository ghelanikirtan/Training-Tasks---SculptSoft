from typing import Optional, List
from src.models.transaction import Transaction
from src.services.database import DatabaseService
from src.services.inventory_service import InventoryService
from src.services.queries import *

class TransactionService(DatabaseService):
    def __init__(self):
        super().__init__()
        self.inventory_service = InventoryService()

    def add_transaction(self, transaction: Transaction) -> int:
        """Add a transaction and update inventory."""
        transaction_details = (
            transaction.product_id,
            transaction.warehouse_id,
            transaction.quantity,
            transaction.transaction_type,
            transaction.reference_id,
            transaction.notes
        )
        
        try:
            # Start a transaction
            self.connection.execute("BEGIN TRANSACTION")
            
            # Add transaction record
            self.cursor.execute(ADD_TRANSACTION, transaction_details)
            transaction_id = self.cursor.lastrowid
            
            # Update inventory based on transaction type
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
                    from src.models.inventory import Inventory
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
            return transaction_id
        except Exception as e:
            # Rollback in case of error
            self.connection.rollback()
            print(f"An error occurred while adding transaction: {e}")
            return None
            
    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]:
        """Get a transaction by its ID."""
        try:
            query = """
            SELECT transaction_id, product_id, warehouse_id, quantity, transaction_type, 
                   reference_id, notes, transaction_date
            FROM transactions
            WHERE transaction_id = ?
            """
            
            self.cursor.execute(query, (transaction_id,))
            row = self.cursor.fetchone()
            
            if row:
                return Transaction(
                    transaction_id=row[0],
                    product_id=row[1],
                    warehouse_id=row[2],
                    quantity=row[3],
                    transaction_type=row[4],
                    reference_id=row[5],
                    notes=row[6],
                    transaction_date=row[7]
                )
            return None
        except Exception as e:
            print(f"An error occurred [get_transaction_by_id]: {e}")
            return None
        
    def get_transactions_by_product(self, product_id: int) -> List[Transaction]:
        """Get all transactions for a specific product."""
        try:
            query = """
            SELECT transaction_id, product_id, warehouse_id, quantity, transaction_type, 
                   reference_id, notes, transaction_date
            FROM transactions
            WHERE product_id = ?
            ORDER BY transaction_date DESC
            """
            
            self.cursor.execute(query, (product_id,))
            records = self.cursor.fetchall()
            transactions = []
            
            for row in records:
                transactions.append(Transaction(
                    transaction_id=row[0],
                    product_id=row[1],
                    warehouse_id=row[2],
                    quantity=row[3],
                    transaction_type=row[4],
                    reference_id=row[5],
                    notes=row[6],
                    transaction_date=row[7]
                ))
            
            return transactions
        except Exception as e:
            print(f"An error occurred [get_transactions_by_product]: {e}")
            return []