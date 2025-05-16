from pydantic import BaseModel
from typing import Union, Any, List, Optional

class BOOK(BaseModel):
    # book_id: int
    title: str 
    author: str
    genre: str
    publisher: str
    
    
    