from typing import List, Optional

from sqlalchemy import create_engine


# Constants:
URL = 'sqlite:///database/database.db'

# create engine [to connect SQLite Database]
engine = create_engine(URL)
conn = engine.connect()
print(conn)

# if __name__ == '__main__':
    # pass

 