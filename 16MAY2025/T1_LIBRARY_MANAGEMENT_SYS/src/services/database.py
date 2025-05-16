import os 
import sqlite3
from datetime import date
from typing import Optional, Literal 
from src.models.book import BOOK
from src.models.member import MEMBER 
from src.models.transaction import TRANSACTION
from src.services.queries import *

class DatabaseService:
    """Service class for database operations.
    
    This class manages all the CRUD operations like add book, delete book, update transaction, delete transaction, add member, delete member, etc...
    """
    def __init__(self):
        """Initialize the DatabaseService by establishing the connection."""
        self.database_path = os.path.join('database', 'database.db')
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        
        
    def make_migrations(self):
        """Creates a tables and database."""
        sql_scripts = None
        with open('schema.sql') as sq:
            sql_scripts = sq.read()
            sql_scripts = sql_scripts.split(';')
            
        if sql_scripts:
            for script in sql_scripts:
                self.cursor.execute(str(script))
            self.connection.commit()
    
    def close_connections(self):
        try: 
            self.connection.close()
        except Exception as e:
            print(f"Unable to close the connection: {e}")
        else:
            print(f"DB Connection closed successfully!")
            
            

    def add_book(self, book: BOOK):
        """Add a new book to the library
        
        :param book: The book object to be added.
        """
        book_details = (
            book.title,
            book.author,
            book.genre,
            book.publisher
        )
        try:
            self.cursor.execute(INSERT_BOOK, book_details)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Book with title '{book.title}' already exists.")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        else: 
            print(f"Book '{book.title}' added successfully.")
            return 
    
    def add_member(self, member: MEMBER):
        """Add a new member to the library.

        :param member: The member object to be added.
        """
        member_details = (
            member.f_name, 
            member.l_name,
            member.email,
            member.phone
        )
        
        try:
            self.cursor.execute(INSERT_MEMBER, member_details)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Member with email '{member.email}' already exists.")
            return
        except Exception as e:
            print(f"An error occured: {e}")
            return
        else: 
            print(f"Member {member.f_name} {member.l_name} Added Successfully!")
            return
    
    
    def delete_book(self, book_id: int):
        """Delete a book from the library.

        :param book_id: The ID of the book to be deleted.
        """
        try:
            query = f"""DELETE FROM books WHERE book_id = {book_id};"""
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Cannot delete Book with id : {book_id}")
        except Exception as e:
            print(f"An error occured {e}")
        else:
            print(f"Deleted Book with id: {book_id}")
            return
    
    
    def delete_member(self, member_id: int):
        """Delete a member from the library.

        :param member_id: The ID of the member to be deleted.
        """
        try:
            query = f"""DELETE FROM members WHERE member_id = {member_id};"""
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Cannot delete Member with id: {member_id}")
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            print(f"Deleted Member with id: {member_id}")
            return
    
    def start_transaction(self, 
                          book_id: int, 
                          member_id: int, 
                          
                          issue_date: date,
                          due_date: date,
                          return_date: Optional[date] = None
                          ):
        """Start a new transaction.

        :param book_id: The ID of the book to be issued.
        :param member_id: The ID of the member who will receive the book.
        """
        
        
        
        pass
    
    def update_transaction(self, transaction: TRANSACTION):
        """Update an existing transaction.

        :param transaction: The transaction object with updated information.
        """ 
        
        
        pass
    
    