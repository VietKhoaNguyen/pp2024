from domains import Student, Course

def input_student():
    student = Student("", "", "", {})
    student.input()
    return student

def input_course():
    course = Course("", "", 0)
    course.input()
    return course