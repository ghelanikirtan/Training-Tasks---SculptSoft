-- E-commerce Reporting Dashboard:

create database business_intelligence;
use business_intelligence;


create table if not exists customers(
	customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table if not exists orders(
	order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_id INTEGER NOT NULL, 
    
    total_amount DECIMAL(10, 2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

create table if not exists products(
	product_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(355),
    category VARCHAR(300),
    price DECIMAL(10,2)
);

create table if not exists order_items(
	order_item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL, 
    quantity INTEGER,
    price DECIMAL(10,2),
    
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

create table if not exists site_visits(
	visit_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    vist_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

