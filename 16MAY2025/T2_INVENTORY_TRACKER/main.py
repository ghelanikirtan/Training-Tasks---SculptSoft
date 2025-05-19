from datetime import datetime
from typing import List, Optional
import time
#
from src.models.product import Product
from src.models.warehouse import Warehouse
from src.models.inventory import Inventory
from src.models.transaction import Transaction

# 
from src.services.database import DatabaseService
from src.services.product_service import ProductService
from src.services.warehouse_service import WarehouseService
from src.services.inventory_service import InventoryService
from src.services.transaction_service import TransactionService



# TESTING MODULES...

prod1 = Product(
    name = 'ACER NITRO 5 15',
    price = 87000,
    category= 'NOTEBOOKS [LAPTOPS]'
)

prod2 = Product(
    name = 'APPLE MAC BOOK AIR M4',
    price = 98000,
    category= 'NOTEBOOKS [LAPTOPS]'
)

prod3 = Product(
    name = 'KEYBOARD REDGEAR',
    price = 3000,
    category= 'Accessories'
)

warehouse1 = Warehouse(
    name = 'AMD NPC',
    location = "Ahmedabad",
    capacity = 500,
    status = 'active'
)

warehouse2 = Warehouse(
    name = 'ADLJ',
    location = 'Gandhinagar',
    capacity = 200,
    status = 'active'
)

# TESTING SERVICES:::::::::::::

services = DatabaseService()
product_services = ProductService(services=services)
warehouse_services = WarehouseService(services=services)
inventory_services = InventoryService(services=services)
transaction_service = TransactionService(services=services)


# Adding products::::
product_services.add_product(prod1)
product_services.add_product(prod2)
product_services.add_product(prod3)
# Adding warehouses::::
warehouse_services.add_warehouse(warehouse1) 
warehouse_services.add_warehouse(warehouse2) 

# Display all products and warehouses:
products = product_services.get_all_products()
warehouses = warehouse_services.get_all_warehouses()
print('Products::::::')
for product in products:
    print(product)
print('-'*50)
print('Warehouses::::::')
for warehouse in warehouses:
    print(warehouse)

# Add items in the inventory....
# inventory1 = Inventory(
#     product_id=1, #Acer nitro laptop
#     warehouse_id=1,
#     quantity=10,
#     last_restock_date = datetime.now()
# )
# inventory2 = Inventory(
#     product_id=2, #Apple Mac Book laptop
#     warehouse_id=1,
#     quantity=20,
#     last_restock_date = datetime.now()
# )
# inventory3 = Inventory(
#     product_id=3, #Keyboard
#     warehouse_id=2,
#     quantity=30,
#     last_restock_date = datetime.now()
# )


# Performing Transactions Now:::::::
transactions = [
    # Adding items...
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
    )
]


for transaction in transactions:
    transaction_service.add_transaction(transaction)
    print("trying to add transaction...")
    time.sleep(0.5)
print('-'*50)
print('Inventory Items::::::')
items = inventory_services.get_all_inventory()
for item in items:
    print(item)

    
print('-'*50)
print('Transactions::::::')
tns = transaction_service.get_all_transactions()
for transaction in transactions:
    print(transaction)



    
    

