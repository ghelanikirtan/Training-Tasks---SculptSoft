from typing import Optional, List
from src.models.product import Product
from src.services.database import DatabaseService
from src.services.queries import *

class ProductService(DatabaseService):
    def __init__(self):
        super().__init__()

    def add_product(self, product: Product) -> int:
        """Add a product to the products table."""
        product_details = (
            product.name,
            product.description,
            product.sku,
            product.price,
            product.category
        )
        
        try:
            self.cursor.execute(ADD_PRODUCT, product_details)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"An error occurred while adding product: {e}")
            return None
            
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Get a product by its ID."""
        try:
            query = """
            SELECT product_id, name, description, sku, price, category, created_at, updated_at 
            FROM products
            WHERE product_id = ?
            """
            
            self.cursor.execute(query, (product_id,))
            row = self.cursor.fetchone()
            
            if row:
                return Product(
                    product_id=row[0],
                    name=row[1],
                    description=row[2],
                    sku=row[3],
                    price=row[4],
                    category=row[5],
                    created_at=row[6],
                    updated_at=row[7]
                )
            return None
        except Exception as e:
            print(f"An error occurred [get_product_by_id]: {e}")
            return None
        
    def get_all_products(self) -> List[Product]:
        """Get all products."""
        try:
            query = """
            SELECT product_id, name, description, sku, price, category, created_at, updated_at 
            FROM products
            """
            
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            products = []
            
            for row in records:
                products.append(Product(
                    product_id=row[0],
                    name=row[1],
                    description=row[2],
                    sku=row[3],
                    price=row[4],
                    category=row[5],
                    created_at=row[6],
                    updated_at=row[7]
                ))
            
            return products
        except Exception as e:
            print(f"An error occurred [get_all_products]: {e}")
            return []
            
    def update_product(self, product: Product) -> bool:
        """Update a product."""
        try:
            product_details = (
                product.name,
                product.description,
                product.sku,
                product.price,
                product.category,
                product.product_id
            )
            
            self.cursor.execute(UPDATE_PRODUCT, product_details)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [update_product]: {e}")
            return False
            
    def delete_product(self, product_id: int) -> bool:
        """Delete a product."""
        try:
            self.cursor.execute(DELETE_PRODUCT, (product_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"An error occurred [delete_product]: {e}")
            return False