import time
from typing import List
# 
from src.models.product import Product
from src.models.warehouse import Warehouse
from src.models.inventory import Inventory
from src.models.transaction import Transaction
# 
from src.services.database import DatabaseService
from src.services.product_services import ProductService
from src.services.warehouse_services import WarehouseService
from src.services.inventory_services import InventoryService
from src.services.transaction_services import TransactionService



services = DatabaseService()
product_services = ProductService(services)
warehouse_services = WarehouseService(services)
transaction_services = TransactionService(services)

services.make_migrations()

products: List[Product] = [
    Product(
        name = "ACER NITRO 5 15",
        price = 85000.0,
        category = "NOTEBOOK"
    ),
    Product(
        name = 'APPLE MAC BOOK AIR M4',
        price = 98000,
        category= 'NOTEBOOKS [LAPTOPS]'
    ),
    Product(
        name = 'KEYBOARD REDGEAR',
        price = 3000,
        category= 'Accessories'
    ),
]

warehouses: List[Warehouse] = [
    Warehouse(
        name = 'AMD NPC',
        location = "Ahmedabad",
        capacity = 500,
        status = 'active'
    ),
    Warehouse(
        name = 'ADLJ',
        location = 'Gandhinagar',
        capacity = 200,
        status = 'active'
    )
]


# TESTING ALL SERVICES:

for product in products:
    product_services.add_product(product)

for warehouse in warehouses:
    warehouse_services.add_warehouse(warehouse)
    
# Fetch all Details:
# print(f"PRODUTS::::")
# pds = product_services.get_all_products()
# whs = warehouse_services.get_all_warehouses()
# for p in pds:
#     print(p)
# print('-'*50)
# print(f"WAREHOUSES::::")
# for w in whs:
#     print(w)


# Transactions::::

transactions: List[Transaction] = [
    Transaction(
        product_id=1,
        warehouse_id=1,
        quantity=10,
        transaction_type='in',
    ),
    Transaction(
        product_id=2,
        warehouse_id=1,
        quantity=20,
        transaction_type='in',
    ),
    Transaction(
        product_id=3,
        warehouse_id=2,
        quantity=10,
        transaction_type='in',
    ),
    
    # Removing items...
    Transaction(
        product_id=1,
        warehouse_id=1,
        quantity=3,
        transaction_type='out',
    ),
    Transaction(
        product_id=2,
        warehouse_id=1,
        quantity=30,
        transaction_type='out',
    )
]

for transaction in transactions:
    transaction_services.initiate_transaction(transaction)
    time.sleep(0.2)

# print('-'*50)
# print(f"TRANSACTIONS::::")
# tns = transaction_services.get_all_transactions()
# for t in tns:
#     print(t)
