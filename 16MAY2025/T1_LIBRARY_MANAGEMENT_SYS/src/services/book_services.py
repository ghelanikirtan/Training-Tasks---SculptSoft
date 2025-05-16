from typing import List, Optional
from src.services.database import DatabaseService
from src.models.book import BOOK

class BookServices(DatabaseService):
    
    def __init__(self):
        super().__init__()
        
    
    def get_book_by_id(self, book_id: int) -> tuple[int, BOOK]:
        
        try:
            query = f"""
            SELECT book_id, title, author, genre, publisher from books
            WHERE book_id = {book_id};
            """
            records = self.cursor.execute(query)
            records = records.fetchall()
            
            book_id: int = None
            book: BOOK = None
            for row in records:
                book_id = row[0]
                book = BOOK(
                    title = row[1],
                    author = row[2],
                    genre = row[3],
                    publisher = row[4]  
                )
                
                
            return (book_id, book)
        except Exception as e:
            print(f"An Error Occured [get_book_by_id()]: {e}")
            return None
        
    def get_all_books(self) -> List[tuple[int, BOOK]]:
        
        try:
            query = f"""
            SELECT book_id, title, author, genre, publisher from books;
            """
            records = self.cursor.execute(query)
            records = records.fetchall()
            
            books = []
            for row in records:
                book_id = row[0]
                book = BOOK(
                    title = row[1],
                    author = row[2],
                    genre = row[3],
                    publisher = row[4]  
                )
                books.append((book_id, book))
                
            return books
        
        except Exception as e:
            print(f"An Error Occured [get_book_by_id()]: {e}")
            return []
        
        