from pydantic import BaseModel
from typing import Union, Any, List, Optional

class MEMBER(BaseModel):
    # member_id: int
    f_name: str
    l_name: str
    email: str
    phone: str