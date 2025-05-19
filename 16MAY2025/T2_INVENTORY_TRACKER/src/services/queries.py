# Product Queries
ADD_PRODUCT = """
INSERT INTO products (name, price, category)
VALUES (?, ?, ?);
"""

UPDATE_PRODUCT = """
UPDATE products
SET name = ?, description = ?, sku = ?, price = ?, category = ?, updated_at = CURRENT_TIMESTAMP
WHERE product_id = ?
"""

DELETE_PRODUCT = """
DELETE FROM products
WHERE product_id = ?
"""

# Warehouse Queries
ADD_WAREHOUSE = """
INSERT INTO warehouses (name, location, capacity, status)
VALUES (?, ?, ?, ?);
"""

UPDATE_WAREHOUSE = """
UPDATE warehouses
SET name = ?, location = ?, capacity = ?, status = ?, updated_at = CURRENT_TIMESTAMP
WHERE warehouse_id = ?
"""

DELETE_WAREHOUSE = """
DELETE FROM warehouses
WHERE warehouse_id = ?
"""

# Inventory Queries
ADD_INVENTORY = """
INSERT INTO inventory (product_id, warehouse_id, quantity)
VALUES (?, ?, ?);
"""

UPDATE_INVENTORY = """
UPDATE inventory
SET quantity = ?, last_restock_date = ?, updated_at = CURRENT_TIMESTAMP
WHERE product_id = ? AND warehouse_id = ?
"""

DELETE_INVENTORY = """
DELETE FROM inventory
WHERE inventory_id = ?
"""

# Transaction Queries
ADD_TRANSACTION = """
INSERT INTO transactions (product_id, warehouse_id, quantity, transaction_type)
VALUES (?, ?, ?, ?);
"""