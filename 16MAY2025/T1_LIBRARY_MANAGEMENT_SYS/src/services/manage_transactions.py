from typing import List, Optional 
from src.services.database import DatabaseService
from src.models.transaction import TRANSACTION


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
        
    def borrow_books(self, member_id, book_id):
        """Which Member borrows which book here is taken care off..."""
        
        mem_query = f"""
            SELECT member_id, f_name, l_name, email, phone from members
            where member_id = {member_id};
            """
        
        book_query = f"""
            SELECT book_id, title, author, genre, publisher from books
            WHERE book_id = {book_id};
            """
        
            
        
            
        
        
        