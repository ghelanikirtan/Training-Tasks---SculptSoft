from typing import Optional, List
from src.models.product import Product
from src.services.database import DatabaseService
from src.services.queries import *

class ProductService:
    def __init__(self, services: DatabaseService = None):
        self.services = DatabaseService()
        self.services.make_migrations()
        self.cursor = self.services.cursor
        self.connection = self.services.connection

    def add_product(self, product: Product):
        """Add a product to the products table."""
        product_details = (
            product.name,
            product.price,
            product.category
        )
        
        try:
            self.cursor.execute(ADD_PRODUCT, product_details)
            self.connection.commit()
            # return self.cursor.lastrowid
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print(f"Product {product.name} @ {product.price}/- Added Successfully!")
            
            
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Get a product by its ID."""
        try:
            query = f"""
            SELECT product_id, name, price, category, created_at, updated_at 
            FROM products
            WHERE product_id = {product_id};
            """
            
            records = self.cursor.execute(query).fetchall()
            product: Product = None 
            for row in records:
                product = Product(
                    product_id=row[0],
                    name=row[1],
                    price=row[2],
                    category=row[3],
                    created_at=row[4],
                    updated_at=row[5]
                )
            return product
        except Exception as e:
            print(f"An error occurred [get_product_by_id]: {e}")
            return None
        
    def get_all_products(self) -> List[Product]:
        """Get all products."""
        try:
            query = f"""
            SELECT product_id, name, price, category, created_at, updated_at 
            FROM products;
            """
            
            records = self.cursor.execute(query).fetchall()
            products:List[Product] = []
            for row in records:
                products.append(Product(
                    product_id=row[0],
                    name=row[1],
                    price=row[2],
                    category=row[3],
                    created_at=row[4],
                    updated_at=row[5]
                ))
            
            return products
        except Exception as e:
            print(f"An error occurred [get_all_products]: {e}")
            return []
            
    def update_product(self, product: Product) -> bool:
        """Update a product."""
        try:
            
            query = f"""
            UPDATE products
            SET name = {product.name}, price = {product.price}, category = {product.category}, updated_at = CURRENT_TIMESTAMP
            WHERE product_id = {product.product_id}
            """
                        
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [update_product]: {e}")
            return False
            
    def delete_product(self, product_id: int) -> bool:
        """Delete a product."""
        try:
            query = f"""
            DELETE FROM products
            WHERE product_id = {product_id};
            """
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [delete_product]: {e}")
            return False