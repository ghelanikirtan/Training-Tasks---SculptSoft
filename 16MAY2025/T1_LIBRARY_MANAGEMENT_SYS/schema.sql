create table if not exists members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(15)
);

create table if not exists books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(400),
    author VARCHAR(255),
    genre VARCHAR(255),
    publisher VARCHAR(255)
); 

create table if not exists transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INT,
    member_id INT, 
    issue_date DATE,
    return_date DATE,
    fine_amount DECIMAL(6,2),
    status VARCHAR(50),

    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

