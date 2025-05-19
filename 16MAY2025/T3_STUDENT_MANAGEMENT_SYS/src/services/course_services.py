from typing import Optional, List
from src.models.course import Course
from src.services.database import DatabaseService
from src.services.queries import *


class CourseService():
    def __init__(self, services: DatabaseService = None):
        self.services = DatabaseService()
        self.services.make_migrations()
        self.cursor = self.services.cursor
        self.connection = self.services.connection
        
    def add_course(self, course: Course):
        """Add Coursee to the courses table..."""
        
        course_details = (
            course.course_code,
            course.course_name,
            course.credits,
            course.department
        )
        
        try:
            self.cursor.execute(ADD_COURSE, course_details)
            self.connection.commit()
        except Exception as e:
            print(f"An error occured: {e}")
        else:
            print(f"COURSE [{course.course_code}]: {course.course_name} added successfully!")

    
    def get_course_by_id(self, course_id: int) -> Optional[Course]:
        
        try:
            query = f"""
            SELECT course_id, course_code, course_name, credits, department FROM courses
            WHERE course_id = {course_id};
            """
            
            records = self.cursor.execute(query).fetchall()
            course: Course  = None
            for row in records:
                course = Course(
                    course_id = row[0],
                    course_code = row[1],
                    course_name = row[2],
                    credits = row[3],
                    department = row[4] 
                )
            
            return course
        
        except Exception as e:
            print(f"An error occured [get_course_by_id]: {e}")
            return None 
        
    
    def get_all_courses(self) -> List[Course]:
        """ 
        """
        try:
            query = f"""
            SELECT course_id, course_code, course_name, credits, department FROM courses;
            """
            
            records = self.cursor.execute(query).fetchall()
            courses: List[Course] = []
            for row in records:
                
                courses.append(Course(
                    course_id = row[0],
                    course_code = row[1],
                    course_name = row[2],
                    credits = row[3],
                    department = row[4] 
                ))
            
            return courses
        
        except Exception as e:
            print(f"An error occured [get_all_courses]: {e}")
            return [] 
        
        
        