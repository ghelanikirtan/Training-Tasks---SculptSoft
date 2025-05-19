from typing import Optional, List
from src.models.grade import Grade
from src.services.database import DatabaseService
from src.services.queries import *


class GradeService():
    
    def __init__(self, services: DatabaseService = None):
        self.services = DatabaseService()
        self.services.make_migrations()
        self.cursor = self.services.cursor
        self.connection =  self.services.connection
        
    def assign_grades(self, grade: Grade):
        """
        """ 
        grade_details = (
            grade.student_id,
            grade.course_id,
            grade.grade
        )
        
        try:
            self.cursor.execute(ADD_GRADE, grade_details)
            self.connection.commit()
        except Exception as e:
            print(f"An error occured: {e}")    
        else:
            print(f"Grade: {grade.grade} Assigned to student_id {grade.student_id} in course_id {grade.course_id} Successfully!")

    
    def get_grade_details(self, student_id:int = None, course_id:int = None) -> List[Grade]:
        """
        """
        try:
            query:str = None
            if student_id and (course_id is None):
                query = f"""
                SELECT grade_id, student_id, course_id, grade FROM grades
                WHERE student_id = {student_id};
                """
            elif course_id and (student_id is None):
                query = f"""
                SELECT grade_id, student_id, course_id, grade FROM grades
                WHERE course_id = {course_id};
                """
            elif student_id and course_id:
                query = f"""
                SELECT grade_id, student_id, course_id, grade FROM grades
                WHERE student_id = {student_id} and course_id = {course_id};
                """
            else:
                query = f"""
                SELECT grade_id, student_id, course_id, grade FROM grades;
                """
                
            if query:
                records = self.cursor.execute(query).fetchall()
                grades: List[Grade] = []
                for row in records:
                    grades.append(
                        Grade(
                            id = row[0],
                            student_id = row[1],
                            course_id = row[2],
                            grade = row[3]
                        )
                    )
                    
                return grades
            
            return []
        except Exception as e:
            print(f"An Error occured [get_grade_details]: {e}")
            return []    
        