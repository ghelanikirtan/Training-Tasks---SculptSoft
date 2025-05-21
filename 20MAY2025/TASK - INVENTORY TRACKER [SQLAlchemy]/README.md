# TASKS - 20TH MAY 2025

1. Convert any one of the mini-project (from 16th May 2025) to SQLAlchemy based.

> - Converted an entire project to SQLAlchemy ORM based...

2. Implement Transactions using `BEGIN`, `COMMIT`, `ROLLBACK`, and `SAVEPOINT`. Also maintained the ACID Properties.

> - Implemented this thing and along with maintaining the Atomicity, Consistency, Isolation, Durability
> - To Check this look into `/main.py` testing file.

- For modules look into :

```
/src/models/transaction.py
/src/models/inventory.py
/src/services/transaction_services.py
/src/services/inventory_services.py
```

3. To implement `GRANT` and `REVOKE` methods in the same project.

> - Created the `User` and `Permission` Table along with `user-permissions` table to maintain MANY-MANY relationship between them. That enables user to a permission to perform `[read | write]` actions in resources `['product', 'warehouse', 'inventory', 'transaction']` as well as REVOKE the same.
>   To Check this look into `/grant_revoke_access.py` testing file.

- For modules look into:

```
/src/models/user.py
/src/models/permission.py
/src/services/permission_manager.py
```
