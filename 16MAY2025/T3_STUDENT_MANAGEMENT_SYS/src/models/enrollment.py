from pydantic import BaseModel
from typing import Optional


class Enrollment(BaseModel):
    id: Optional[int]
    student_id: int 
    course_id: int 
