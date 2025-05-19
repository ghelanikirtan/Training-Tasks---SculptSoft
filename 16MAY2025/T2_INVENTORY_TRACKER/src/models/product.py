from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Product(BaseModel):
    product_id: Optional[int] = None
    name: str
    price: float
    category: Optional[str] = None 
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
            