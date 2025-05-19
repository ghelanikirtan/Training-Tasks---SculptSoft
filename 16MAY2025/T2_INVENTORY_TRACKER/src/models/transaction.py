from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime 

class Transaction(BaseModel):
    transaction_id: Optional[int] = None
    product_id: int
    warehouse_id: int
    quantity: int 
    transaction_type: Literal['in' , 'out', 'transfer']
    transaction_date: Optional[datetime] = None