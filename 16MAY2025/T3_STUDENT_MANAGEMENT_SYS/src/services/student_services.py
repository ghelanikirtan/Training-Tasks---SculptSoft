from typing import Optional, List
from src.models.student import Student
from src.services.database import DatabaseService
from src.services.queries import *

class StudentService():
    def __init__(self, services: DatabaseService = None):
        self.services = DatabaseService()
        self.services.make_migrations()
        self.cursor = self.services.cursor
        self.connection = self.services.connection        
    
    def add_student(self, student: Student):
        """Add student to students table...
        """
        student_details = (
            student.first_name, 
            student.last_name,
            student.email,
            student.dob,
            student.phone,
            student.status
        )
        
        try:
            self.cursor.execute(ADD_STUDENT, student_details)
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            print(f"Student {student.first_name} {student.last_name} added successfully!")
            
    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        
        try:
            query = f"""
            SELECT student_id, first_name, last_name, email, dob, phone, status FROM students 
            WHERE student_id = {student_id};
            """
            
            records = self.cursor.execute(query).fetchall()
            student: Student = None
            for row in records:
                student = Student(
                    student_id = row[0],
                    first_name = row[1],
                    last_name = row[2],
                    email = row[3],
                    dob = row[4],
                    phone = row[5],
                    status = row[6]
                )
            
            return student 
        except Exception as e:
            print(f"An error occurred [get_student_by_id]: {e}")
            return None 
        
        
    def get_all_students(self) -> List[Student]:
        """
        """
        try:
            query = f"""
            SELECT student_id, first_name, last_name, email, dob, phone, status FROM students;
            """
            
            records = self.cursor.execute(query).fetchall()
            students: List[Student] = []
            for row in records:
                
                students.append(
                    Student(
                        student_id = row[0],
                        first_name = row[1],
                        last_name = row[2],
                        email = row[3],
                        dob = row[4],
                        phone = row[5],
                        status = row[6]
                        )
                )
            
            return students 
        except Exception as e:
            print(f"An error occurred [get_all_students]: {e}")
            return []
        
