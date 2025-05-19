from datetime import date
from typing import List

# Models Import
from src.models.student import Student
from src.models.course import Course
from src.models.grade import Grade

# Services Import
from src.services.database import DatabaseService
from src.services.student_services import StudentService
from src.services.course_services import CourseService
from src.services.grade_services import GradeService


stud1 = Student(
    first_name = 'Kirtan',
    last_name = 'Ghelani',
    email = 'kghelani.dev@gmail.com',
    dob = date(2002,9,2),
    phone = '9876543218',
    status = 'active'
)

stud2 = Student(
    first_name = 'Student 2',
    last_name = 'Second Name 3',
    email = 'second_stud@gmail.com',
    dob = date(2002,12,28),
    phone = '9876549878',
    status = 'active'
)

course_ai = Course(
    course_code = 'CS509',
    course_name = 'Artificial Intelligence',
    credits = 4,
    department = 'CSE'
)

course_ml = Course(
    course_code = 'CS409',
    course_name = 'Machine Learning',
    credits = 3,
    department = 'CSE'
)


services  = DatabaseService()

student_services = StudentService(services=services)
course_services = CourseService(services=services)
grade_services = GradeService(services=services)

# Data insertion:
student_services.add_student(stud1)
student_services.add_student(stud2)
# 
course_services.add_course(course_ai)
course_services.add_course(course_ml)

# Fetch and display all:
students: List[Student] = student_services.get_all_students()
courses: List[Course] = course_services.get_all_courses()

for student in students:
    print(student)
print('-'*50)
for course in courses:
    print(courses)    
    
    
# Assigning grade to different students:

# stud1 got 98 marks in AI & 87 marks in ML
grade_stud1_ai = Grade(
    student_id=1,
    course_id=1,
    grade=98
)
grade_stud1_ml = Grade(
    student_id=1,
    course_id=2,
    grade=87
)

# stud2 got 75 marks in ML and 73 marks in AI
grade_stud2_ml = Grade(
    student_id=2,
    course_id=2,
    grade=75
)
grade_stud2_ai = Grade(
    student_id=2,
    course_id=1,
    grade=73
)

grade_services.assign_grades(grade_stud1_ai)
grade_services.assign_grades(grade_stud1_ml)
grade_services.assign_grades(grade_stud2_ai)
grade_services.assign_grades(grade_stud2_ml)

# Get All Grades:
grades: List[Grade] = grade_services.get_grade_details()
print('-'*50)
for grade in grades:
    print(courses)    
