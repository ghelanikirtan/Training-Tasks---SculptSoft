from typing import List, Optional 
from src.services.database import DatabaseService
from src.models.transaction import TRANSACTION
from datetime import datetime, timedelta


class ManageTransactions(DatabaseService):
    
    def __init__(self):
        super().__init__()
    
    def get_transaction_by_id(self, transaction_id:int) -> tuple[int, TRANSACTION]:
        try:
            query = f"""
            SELECT transaction_id, book_id, member_id, issue_date, return_date, fine_amount, status from transactions
            WHERE transaction_id = {transaction_id}
            """
            records = self.cursor.execute(query)
            records = records.fetchall()
            
            trans_id:int= None
            transaction: TRANSACTION = None
            
            for row in records:
                trans_id = row[0]
                transaction =TRANSACTION(
                    book_id = row[1],
                    member_id = row[2],
                    issue_date = row[3],
                    return_date = row[4],
                    fine_amount = row[5],
                    status= row[6],
                )
            return (trans_id, transaction)           
        except Exception as e:
            print(f"An error occured [get_transaction_by_id()]: {e}")
            return None
        
    
    def get_all_transactions(self) -> List[tuple[int, TRANSACTION]]:
        try:
            query = f"""
            SELECT transaction_id, book_id, member_id, issue_date, return_date, fine_amount, status from transactions;
            """
            records = self.cursor.execute(query)
            records = records.fetchall()
            
            transactions = []
            for row in records:
                trans_id = row[0]
                transaction =TRANSACTION(
                    book_id = row[1],
                    member_id = row[2],
                    issue_date = row[3],
                    return_date = row[4],
                    fine_amount = row[5],
                    status= row[6],
                )
                transactions.append((trans_id, transaction))

            return transactions
        
        except Exception as e:
            print(f"An error occured [get_transaction_by_id()]: {e}")
            return []
        
    
    def borrow_books(self, member_id:int, book_id:int) -> int:
        """Which Member borrows which book here is taken care off..."""
        try:
        
            issue_date = datetime.now().date()
            return_date = datetime.now().date() + timedelta(days=14)

            fine_amt = 0        
            transaction:TRANSACTION = TRANSACTION(
                book_id = book_id,
                member_id = member_id,
                issue_date = issue_date.strftime("%Y-%m-%d"),
                return_date = return_date.strftime("%Y-%m-%d"),
                fine_amount = fine_amt,
                status = 'in-progress' 
            )
        
            trans_id = self.start_transaction(transaction)
            return trans_id
        except Exception as e:
            print(f"An error occured [.borrow_books()]: {e}")
            return None        
        
    def check_status(self, trans_id:int):
        
        try:
            query = f"""
            SELECT issue_date, return_date, status, fine_amount from transactions
            WHERE transaction_id = {trans_id}
            """
            records = self.cursor.execute(query)
            res = records.fetchall()
            status = None
            for row in res:
                status = row[0]
            
            return status
              
        except Exception as e:
            print(f"An error occcured: {e}")
            
        
        
        
        
            
        
        
        