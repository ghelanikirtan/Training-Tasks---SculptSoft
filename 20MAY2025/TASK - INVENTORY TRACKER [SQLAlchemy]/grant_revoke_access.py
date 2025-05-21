import time
from typing import List, Optional
from src.models.product import Product
from src.models.warehouse import Warehouse
from src.models.inventory import Inventory
from src.models.transaction import Transaction
from src.models.user import User
from src.models.permission import Permission, user_permissions
# 
from src.services.database import DatabaseService
from src.services.product_services import ProductService
from src.services.warehouse_services import WarehouseService
from src.services.inventory_services import InventoryService
from src.services.transaction_services import TransactionService
from src.services.permission_manager import PermissionManager


services = DatabaseService()
product_services = ProductService(services)
warehouse_services = WarehouseService(services)
transaction_services = TransactionService(services)
permission_manager  = PermissionManager(services)

services.make_migrations()

users = [
    User(
        username="admin",
        password="admin123",  
        email="admin@example.com"
    ),
    User(
        username="warehouse_manager",
        password="manager123",
        email="manager@example.com"
    ),
    User(
        username="viewer",
        password="viewer123",
        email="viewer@example.com"
    )
]


permissions = [
    Permission(
        resource="product",
        action="read"
    ),
    Permission(
        resource="product",
        action="write"
    ),
    Permission(
        resource="warehouse",
        action="read"
    ),
    Permission(
        resource="warehouse",
        action="write"
    ),
    Permission(
        resource="inventory",
        action="read"
    ),
    Permission(
        resource="inventory",
        action="write"
    ),
    Permission(
        resource="transaction",
        action="read"
    ),
    Permission(
        resource="transaction",
        action="write"
    )
]

for user in users:
    permission_manager.add_user(user)

for permission in permissions:
    permission_manager.create_permissions(permission)


# GRANT PERMISSIONS:
admin_id = 1
for i in range(1, 9):
    permission_manager.grant_permission(admin_id, i)

manager_id = 2
for i in [1,3,5,7]:
    permission_manager.grant_permission(manager_id, i)
    
permission_manager.grant_permission(manager_id, 6) # inven. write
permission_manager.grant_permission(manager_id, 8) # trans. write

viewer_id = 3
for i in [1,3,5,7]:
    permission_manager.grant_permission(viewer_id, i)

    

# REVOKE PERMISSIONS:
permission_manager.revoke_permission(viewer_id, 1)
