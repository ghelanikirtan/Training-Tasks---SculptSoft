from pydantic import BaseModel
from typing import Union, Any, List, Optional, Literal
from datetime import datetime, date

class TRANSACTION(BaseModel):
    # transaction_id: int
    book_id: int
    member_id: int
    issue_date: str
    return_date: Optional[str] = None
    fine_amount: Optional[float] = None
    status: Literal['completed' , 'in-progress', 'delayed'] = None