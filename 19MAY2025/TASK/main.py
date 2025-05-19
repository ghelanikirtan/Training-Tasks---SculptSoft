from typing import List, Optional

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import String, ForeignKey, Integer, Column, Float


# Constants:
URL = 'sqlite:///database/database.db'

# create engine [to connect SQLite Database]
engine = create_engine(URL)
conn = engine.connect() 
metadata = MetaData()


# Create Table:
products = Table(
    'products', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Float),
    Column('category', String),
)
metadata.create_all(engine)

# Insert Values into Table:
ins = products.insert().values(
    name = 'ACER NITRO 5',
    price = 87000.5,
    category = 'LAPTOP/NOTEBOOK'
)
conn.execute(ins)
conn.commit()

ins = products.insert()

values = [
    {'id': 2, 'name' : 'APPLE MAC BOOK', 'price': 97000.5, 'category': 'LAPTOP/NOTEBOOK'},
    {'id': 3, 'name' : 'CUPBOARD', 'price': 5412.5, 'category': 'DAILY HOUSEHOLD ITEMS'},
    {'id': 4, 'name' : 'AGARO VACCUM CLEANER', 'price': 6520, 'category': 'DAILY HOUSEHOLD ITEMS'},
]
conn.execute(ins, values)
conn.commit()


# READ VALUES:
op = products.select()
res = conn.execute(op).fetchall()
conn.commit()
for r in res:
    print(r)

op = products.select().where(products.c.id > 2)
res = conn.execute(op).fetchall()
conn.commit()
for r in res:
    print(r)
    
# Update Operation:
up = products.update().where(products.c.id == 2).values(name = 'APPLE MAC BOOK AIR M4')
conn.execute(up)
conn.commit()

# Delete Operation:
dele = products.delete().where(products.c.id == 4)
conn.execute(dele)
conn.commit()