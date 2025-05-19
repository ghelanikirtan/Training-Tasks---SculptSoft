# Product Queries
ADD_PRODUCT = """
INSERT INTO products (name, price, category)
VALUES (?, ?, ?);
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


DELETE_WAREHOUSE = """
DELETE FROM warehouses
WHERE warehouse_id = ?
"""

# Inventory Queries
ADD_INVENTORY = """
INSERT INTO inventory (product_id, warehouse_id, quantity)
VALUES (?, ?, ?);
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