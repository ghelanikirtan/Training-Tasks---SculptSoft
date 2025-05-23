use business_intelligence;

insert INTO customers (name, email) VALUES
('Kirtan Ghelani', 'temp1@example.com'), -- 1
('Ghelani Kirtan', 'temp2@example.com'), -- 2
('First Last', 'temp3@example.com'), -- 3
('Russel Andre', 'temp4@example.com'), -- 4
('Virat Kohli', 'temp5@example.com'), -- 5
('Rohi Sharma', 'temp6@example.com'), -- 6
('MS Dhoni', 'temp7@example.com'), -- 7
('Shubhmam Gill', 'temp8@example.com'), -- 8
('Ishan Kishan', 'temp9@example.com'), -- 9
('KL Rahul', 'temp10@example.com'), -- 10 
('Jasprit Bumrah', 'temp11@example.com'), -- 11
('Mohd. Siraj', 'temp12@example.com'); -- 12


insert into products (name, category, price) VALUES
('Laptop', 'Electronics', 100.00), -- 1
('T-Shirt', 'Clothing', 659.99), -- 2
('Mobile', 'Electronics', 19999.99), -- 3
('Mop', 'Household Equipments', 189.99), -- 4
('Vaccum Cleaner', 'Household Equipments', 5999.99), -- 5
('Jeans', 'Clothing', 1050.00), -- 6
('Laptop', 'Electronics', 99999.99), -- 7
('Skirt', 'Clothing', 979.00), -- 8
('Keyboard', 'Electronics', 3050.00), -- 9
('Cricket Bat', 'Sports Equipments', 3500.00), -- 10
('Mouse', 'Electronics', '1250.59'), -- 11
('Pressure Cooker', 'Kitchen Equipments', '2999.99'), -- 12
('Glass Bowls', 'Kitchen Equipements', '1300.00'), -- 13
('Mattress', 'Bedroom Utilities','2850.99'), -- 14
('Dining Table', 'Furniture', '4566.65'), -- 15
('Sofa Sets', 'Furniture', '45623.68'), -- 16
('VR HEADSETS', 'Electronics', 55499.99); -- 17


INSERT INTO orders (customer_id, total_amount, order_date) VALUES
(1, 21500.58, '2025-03-01'),
(2, 1050.00, '2025-03-02'),
(3, 78999.99, '2025-03-15'),
(4, 1300.00, '2025-04-01'),
(5, 7899.99, '2025-04-12'),
(6, 35666.65, '2025-04-25'),
(7, 1250.59, '2025-05-01'),
(8, 3050.00, '2025-05-05'),
(9, 3500.00, '2025-05-10'),
(10, 5999.99, '2025-05-15'),
(11, 55499.99, '2025-05-20'),
(12, 7850.00, '2025-05-21');


INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 3, 1, 19999.99),
(1, 11, 1, 1250.59),
(2, 6, 1, 1050.00),
(3, 7, 1, 99999.99),
(4, 13, 1, 1300.00),
(5, 5, 1, 5999.99),
(5, 4, 1, 189.99),
(5, 12, 1, 2999.99),
(6, 15, 1, 4566.65),
(6, 8, 2, 979.00),
(7, 11, 1, 1250.59),
(8, 9, 1, 3050.00),
(9, 10, 1, 3500.00),
(10, 5, 1, 5999.99),
(11, 17, 1, 55499.99),
(12, 6, 2, 1050.00),
(12, 2, 1, 659.99);

INSERT INTO site_visits (vist_time) VALUES
('2025-03-01'), ('2025-03-01'), ('2025-03-02'),
('2025-04-01'), ('2025-04-10'), ('2025-04-25'),
('2025-05-01'), ('2025-05-10'), ('2025-05-20'), ('2025-05-21');


