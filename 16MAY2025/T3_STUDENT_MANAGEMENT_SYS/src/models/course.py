from pydantic import BaseModel 
from typing import Optional 


class Course(BaseModel):
    id: Optional[int] = None
    course_code: str
    course_name: str
    credits: int 
    department: Optional[str] = None 
    