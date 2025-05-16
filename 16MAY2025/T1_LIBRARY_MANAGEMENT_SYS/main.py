import sqlite3
import os 
from src.models.book import BOOK
from src.models.member import MEMBER
from src.models.transaction import TRANSACTION
from src.services.book_services import BookServices
from src.services.database import DatabaseService
from src.services.manage_transactions import ManageTransactions
from src.services.members_services import MemberServices
from src.services.book_services import BookServices


# BOOKS ->
book1 = BOOK(
    title='TEMP 1',
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

# MEMBERS ->
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
manage_books = BookServices()
manage_transactions = ManageTransactions()
manage_members = MemberServices()

# make migrations:
services.make_migrations()

# Let's add book to a Libaray:
services.add_book(book1)
services.add_book(book2)
services.add_book(book3)
print("ADDED 3 Books to lib...")

# Let's add members to a Library
services.add_member(member1)
services.add_member(member2)
print("Added 2 Memberships")






    
    