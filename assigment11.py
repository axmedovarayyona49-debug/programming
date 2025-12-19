def enroll_student(student_db, course_db, student_id, course_code):  
    if student_id not in student_db or course_code not in course_db:
        raise KeyError("Record not found")
    student = student_db[student_id]
    if course_code in student["current_courses"]:
        raise ValueError("Already enrolled")
    prereq = course_db[course_code].get("prereq")
    if prereq is not None:
        if prereq not in student["passed_courses"]:
            raise ValueError(f"Missing Prereq: {prereq}")
    student["current_courses"].append(course_code)
    return True
def process_enrollments(student_db, course_db, request_list):
    successful = []
    failed = []
    for student_id, course_code in request_list:
        try:
            enroll_student(student_db, course_db, student_id, course_code)
            successful.append(student_id)
        except KeyError as e:
            print(f"Enrollment failed for {student_id} in {course_code}: '{e}'")
            failed.append(student_id)
        except ValueError as e:
          print(f"Enrollment failed for {student_id} in {course_code}: {e}")
            failed.append(student_id)   
    return {"successful": successful, "failed": failed}
courses = {
    "CS101": {"prereq": None},
    "CS102": {"prereq": "CS101"}
}
students = {
    "Alice": {"passed_courses": ["CS101"], "current_courses": []},
    "Bob": {"passed_courses": [], "current_courses": []}
}
requests = [
    ("Alice", "CS102"),   
    ("Bob", "CS102"),    
    ("Charlie", "CS101"), 
    ("Alice", "CS102")    
]
result = process_enrollments(students, courses, requests)
print(result)
