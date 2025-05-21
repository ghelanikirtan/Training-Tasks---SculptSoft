from typing import List, Optional
from sqlalchemy import select, update, delete
from sqlalchemy import and_
from sqlalchemy.exc import SQLAlchemyError

from src.models.transaction import Transaction
from src.models.inventory import Inventory
from src.services.database import DatabaseService
from src.services.inventory_services import InventoryService


class TransactionService:
    
    def __init__(self, services: DatabaseService = None):
        self.services = services if services else DatabaseService()
        self.engine = self.services.engine
        self.conn = self.services.conn
        self.Session = self.services.Session
        # 
        self.inventory_services = InventoryService()
        self.savepoints: List = []
        
    def initiate_transaction(self, transaction: Transaction):
        inventory: Inventory = None
        session = self.Session() # creating session...
        try:
            # Transaction Begin:
            session.begin()
            
            # chckpnt 1
            self.savepoints.append(session.begin_nested())
            
            session.add(transaction)
            session.flush() # sends the changes to the database but will not commit in the db.
            # chckpnt 2
            self.savepoints.append(session.begin_nested())
            
            inventory = self.inventory_services.get_inventory(product_id=transaction.product_id,
                                                              warehouse_id=transaction.warehouse_id,
                                                              session=session)

            if inventory:
                if transaction.transaction_type == 'in':
                    inventory.quantity += transaction.quantity
                elif transaction.transaction_type == 'out':
                    inventory.quantity -= transaction.quantity
                    if inventory.quantity < 0:
                        raise ValueError(f"Insufficient Inventory Items")    
                
                self.inventory_services.update_inventory(inventory_item=inventory, session=session)
            else:
                if transaction.transaction_type == "in":
                    new_inventory = Inventory(
                        product_id = transaction.product_id,
                        warehouse_id = transaction.warehouse_id,
                        quantity = transaction.quantity
                    )
                    
                    self.inventory_services.add_inventory(new_inventory, session)
                else:
                    raise ValueError(f"Cannot Perform Transaction on non-existing inventory.")

            self.savepoints.append(session.begin_nested())
            session.commit()    


        except Exception as e:
            print(f"Transaction Failed [rolling back]: {e}")
            session.rollback()
        
        finally:
            print(f"Closing Session!")
            session.close()
            
            
    def get_transaction_by_id(self, transaction_id:int) -> Optional[Transaction]:
        q = select(Transaction).where(Transaction.transaction_id == transaction_id)
        session = self.Session()
        transaction: Transaction = session.execute(q).scalars().first()
        session.close()
        del session
        return transaction
    
    def get_all_transactions(self) -> List[Transaction]:
        q = select(Transaction)
        session = self.Session()
        transactions: List[Transaction] = session.execute(q).scalars().all()
        session.close()
        del session
        return transactions

        
    def get_savepoints_list(self) -> List:
        return self.savepoints
    
