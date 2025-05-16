INSERT_BOOK = """
INSERT INTO books (title, author, genre, publisher)
VALUES (?, ?, ?, ?);
"""

INSERT_MEMBER = """
INSERT INTO members (f_name, l_name, email, phone)
VALUES (?, ?, ?, ?);
"""

ADD_TRANSACTION = """
INSERT INTO transactions (book_id, member_id, issue_date, return_date, fine_amount, status)
VALUES (?,?,?,?,?,?);
"""


DELETE_TRANSACTION = """
DELETE FROM transactions
WHERE transaction_id =?;
"""





