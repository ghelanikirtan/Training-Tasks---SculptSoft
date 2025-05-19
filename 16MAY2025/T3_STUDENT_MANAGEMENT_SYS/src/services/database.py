import os 
import sqlite3
from datetime import datetime
from pathlib import Path

class DatabaseService:
    """Service class for database operations."""
    
    def __init__(self):
        """Initialize the DatabaseService by establishing the database connection."""
        self.database_path = os.path.join('database', 'database.db')
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
    
    def make_migrations(self):
        """Create tables and database."""
        sql_scripts = None 
        with open('schema.sql', 'r') as sq:
            sql_scripts = sq.read()
            sql_scripts = sql_scripts.split(';')
        
        if sql_scripts:
            for script in sql_scripts:
                self.cursor.execute(str(script))
            self.connection.commit()
    
    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(f"Unable to close the connection: {e}")
        else:
            print(f"DB Connection closed successfully!")
    
    