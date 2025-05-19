## TASK [19TH MAY 2025]:

1. Set up a SQLite database and connect it with SQLAlchemy.
2. Create a model (e.g., User or Product) and perform CRUD operations.
3. Write a script to insert and query data using SQLAlchemy’s ORM.

---

TASKS Completed:

1. Done with setting up the sqlite database and established the connection with the same using sqlalchemy libarary as follow:

```
from sqlalchemy import create_engine

# Constants:
URL = 'sqlite:///database/database.db'

# create engine [to connect SQLite Database]
engine = create_engine(URL)
conn = engine.connect()
```

2. Create a Model (Product) and Perform CRUD Operations.

- Performed CRUD Operation on the created Product table.

3. Write a Script to insert and query data using SQLAlchemy's ORM.

- Also done with the insert, select, delete, update query operations using basic Sqlalchemy.

NOTE: Have to explore in-depth about `sqlalchemy.orm` functions
