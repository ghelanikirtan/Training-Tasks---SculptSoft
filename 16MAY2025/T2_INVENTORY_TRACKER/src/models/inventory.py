from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime 

class Inventory(BaseModel):
    inventory_id: Optional[int] = None
    product_id: int
    warehouse_id: int 
    quantity: int = 0
    last_restock_date: Optional[datetime] = None
    craeted_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    