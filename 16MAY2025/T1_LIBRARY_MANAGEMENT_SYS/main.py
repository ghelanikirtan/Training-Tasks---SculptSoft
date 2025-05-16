import sqlite3
import os 
from src.models.book import BOOK
from src.models.member import MEMBER
from src.models.transaction import TRANSACTION
from src.services.database import DatabaseService

# DATABASE_PATH = os.path.join('database', 'database.db')
# conn = sqlite3.connect(DATABASE_PATH)


book1 = BOOK(
    title='TEMP',
    author='F. Scott ',
    genre='lassic',
    publisher='Charles Scribner\'s Sons'
)

book2 = BOOK(
    title='TEMP 2',
    author='F. Scott ',
    genre='SClassic',
    publisher='Sons'
)

book3 = BOOK(
    title='TEMP 3',
    author='Scott F',
    genre='Classic C',
    publisher='Scribner\'s Sons'
)

member1 = MEMBER(
    f_name = 'KIRTAN',
    l_name = 'Ghelani',
    email = 'kghelani.dev@gmail.com',
    phone = '8977895462'
)

member2 = MEMBER(
    f_name = 'GHELANI',
    l_name = 'PATEL',
    email = 'email2@gmail.com',
    phone = '8965124853'
)


services = DatabaseService()

# make migrations:
services.make_migrations()

# add book to the library:
services.add_book(book=book1)

# remove book from the library:
services.delete_book(book_id=int(2))







    
    