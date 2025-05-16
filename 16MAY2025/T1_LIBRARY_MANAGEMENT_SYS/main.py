import sqlite3
import os 
from src.models.book import BOOK
from src.models.member import MEMBER
from src.models.transaction import TRANSACTION
from src.services.database import DatabaseService

# DATABASE_PATH = os.path.join('database', 'database.db')
# conn = sqlite3.connect(DATABASE_PATH)


book = BOOK(
    title='TEMP',
    author='F. Scott ',
    genre='Classic',
    publisher='Charles Scribner\'s Sons'
)


services = DatabaseService()

# make migrations:
# services.make_migrations()

# add book to the library:
# services.add_book(book=book)

# remove book from the library:
services.delete_book(book_id=int(2))







    
    