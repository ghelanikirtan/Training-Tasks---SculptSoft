ADD_STUDENT = """
INSERT INTO students (first_name, last_name, email, dob, phone, status) 
VALUES (?, ?, ?, ?, ?, ?)
"""

ADD_COURSE = """
INSERT INTO courses (course_code, course_name, credits, department)
VALUES (?, ?, ?, ?)
"""

ADD_ENROLLMENT = """
INSERT INTO enrollments (student_id, course_id)
VALUES (?, ?)
"""

ADD_GRADE = """
INSERT INTO grades (student_id, course_id, grade)
VALUES (?, ?, ?)
"""

