from pydantic import BaseModel
from typing import List, Optional, Literal 
from datetime import date

class Student(BaseModel):
    id: Optional[int]
    first_name : str
    last_name: str
    email: str
    dob: Optional[date] = None 
    phone: Optional[str] = None 
    status: Literal['active', 'inactive', 'graduated', 'suspended'] = 'active'


    