"""Student Mark Management System"""
def display_menu():
    print("\nStudent Mark Management System")
    print("1. Input number of students")
    print("2. Input student information")
    print("3. Input number of courses")
    print("4. Input course information")
    print("5. Select a course and input marks for students")
    print("6. List courses")
    print("7. List students")
    print("8. Show student marks for a given course")
    print("9. Exit")

# Add students -> class
def Num_stu(): # Number of students
    try:
        num = int(input("Num of stu/class "))
        print("Number of student choose: %d" %num)
        return num
    except ValueError:
        print("Wrong, choose again")
        return Num_stu()

# Add student info
def Stu_info(students): #Infomation of students
    student_Id = input("Stu-Id: ")
    name = input("Name: ")
    dob = input("Date of Birth: ")
    if student_Id in students:
        print("Exist -> Wrong")
    else:
        students[student_Id] = {"name": name, "dob": dob, "marks": {}}
        print("Student %s (Id: %s)" % (name, student_Id))

# Add Num-courses
def Courses(): #Number of courses
    try:
        num = int(input("Number of courses: "))
        print("Number of course choose: %d" % num)
        return num
    except ValueError:
        print("Wrong, choose again")
        return Courses()

# Add course info
def Course_info(courses): #Infomation of courses
    course_Id = input("Course Id: ")
    name = input("Course Name: ")
    if course_Id in courses:
        print("Exists -> Wrong")
    else:
        courses[course_Id] = name
        print("Course %s (Id: %s)" % (name, course_Id))

# Add marks/course
def Mark_c(students, courses): # Marks for each courses
    course_Id = input("Enter Course Id: ")
    if course_Id not in courses:
        print("C_Id not found.") # Course
    else:
        print("Inputting marks for course: %s (Id: %s)" % (courses[course_Id], course_Id))
        for student_Id, student in students.items():
            try:
                mark = float(input("Enter mark for %s (Id: %s): " % (student['name'], student_Id)))
                student["marks"][course_Id] = mark
                print(f"Mark for {student['name']} recorded successfully.")
            except ValueError:
                print("Wrong, choose again")

# List courses
def list_courses(courses):
    if not courses:
        print("Unavailable")
    else:
        print("\nCourses:")
        for course_Id, name in courses.items():
            print(f"{course_Id}: {name}")

#List students
def list_students(students):
    if not students:
        print("No students available.")
    else:
        print("\nStudents:")
        for student_Id, data in students.items():
            print(f"Id: {student_Id}, Name: {data['name']}, DoB: {data['dob']}")

# Student marks/course
def show_student_marks_for_course(students, courses):
    course_Id = input("Enter Course Id: ")
    if course_Id not in courses:
        print("Course Id not found.")
    else:
        print(f"\nMarks for {courses[course_Id]} (Id: {course_Id}):")
        for student_Id, student in students.items():
            mark = student["marks"].get(course_Id, None)
            if mark is not None:
                print(f"{student['name']} (Id: {student_Id}): {mark}")
            else:
                print(f"{student['name']} (Id: {student_Id}): No mark available.")

# Main program loop
def main():
    students = {}
    courses = {}
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            Num_stu()
        elif choice == "2":
            Stu_info(students)
        elif choice == "3":
            Courses()
        elif choice == "4":
            Course_info(courses)
        elif choice == "5":
            Mark_c(students, courses)
        elif choice == "6":
            list_courses(courses)
        elif choice == "7":
            list_students(students)
        elif choice == "8":
            show_student_marks_for_course(students, courses)
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("InvalId choice. Please try again.")

if __name__ == "__main__":
    main()
