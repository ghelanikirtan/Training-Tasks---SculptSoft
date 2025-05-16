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

# Displaying all the books
books = manage_books.get_all_books()
print(f"BOOKS AVAILABLE TO BORROW:")
for (book_id, book) in books:
    print(f"""{book_id}. {book.title} by {book.author} [{book.genre} {book.publisher}]""")
print('-'*75)

# Displaying all the persons with memberships:
members = manage_members.get_all_members()
print(f"MEMBERS who can borrow books:")
for (member_id, member) in members:
    print(f"""{member_id}. {member.f_name} {member.l_name} | {member.email} | {member.phone}.""")
print('-'*75)

# Let's suppose 1st member is borrowing book with id 2
transaction_id  = manage_transactions.borrow_books(
    member_id=1,
    book_id=2
)

# Report for the transaction
print(f"Transaction Status!")    
transaction_status = manage_transactions.check_status(trans_id=transaction_id)
print(f"STATUS FOR transaction_id ({transaction_id}): {transaction_status}")    
# 
print(f"Report for the transaction!")
trans_id, trans_details = manage_transactions.get_transaction_by_id(transaction_id)
print(f"""TRANSACTION ID: {transaction_id}. 
      BOOK ID: {trans_details.book_id}
      MEMBER ID: {trans_details.member_id}
      
      ISSUE DATE: {trans_details.issue_date}
      RETURN DATE: {trans_details.return_date}
      
      FINE AMOUNT: {trans_details.fine_amount}
      STATUS: {trans_details.status}
      """)