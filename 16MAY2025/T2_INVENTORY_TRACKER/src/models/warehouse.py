from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime 

class Warehouse(BaseModel):
    warehouse_id: Optional[int] = None
    name: str
    location: str
    capacity: Optional[int]
    status: Literal['active', 'inactive', 'maintenance'] = 'active'
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
