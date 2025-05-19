from pydantic import BaseModel
from typing import Optional 

class Grade(BaseModel):
    id: Optional[int] = None
    student_id: int
    course_id: int 
    grade: float 
    