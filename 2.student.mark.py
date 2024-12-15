class Person:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob

    # Encapsulation: 
    # Getter methods for private attributes
    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    # Polymorphism: 
    # Define a common input method
    def input(self):
        self.__name = input("Enter name: ")
        self.__dob = input("Enter Date of Birth (DD/MM/YYYY): ")

    def __str__(self):
        return f"Name: {self.__name}, DoB: {self.__dob}"


class Student(Person):
    def __init__(self, student_id, name, dob, marks=None):
        super().__init__(name, dob)  # Call the constructor of Person
        self.__student_id = student_id
        self.__marks = marks if marks is not None else {}

    # Encapsulation: 
    # Getter methods for private attributes
    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, course_id, mark):
        self.__marks[course_id] = mark

    # Polymorphism: 
    # Input for student-specific attributes
    def input(self):
        super().input()  # Call the input method from Person
        self.__student_id = input("Enter student ID: ")

    # Display student information
    def __str__(self):
        marks_str = ", ".join([f"{course}: {mark}" for course, mark in self.__marks.items()])
        return f"StudentID: {self.__student_id}, {super().__str__()}, Marks: {marks_str}"


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    # Encapsulation:
    # Getter methods for private attributes
    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    # Polymorphism: 
    # Input for course-specific attributes
    def input(self):
        self.__course_id = input("Enter course ID: ")
        self.__course_name = input("Enter course name: ")

    # Display course information
    def __str__(self):
        return f"CourseID: {self.__course_id}, Name: {self.__course_name}"


class School:
    def __init__(self):
        self.__students = []
        self.__courses = []

    # Encapsulation: 
    # Getter methods for private attributes
    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    # Methods to add student and course to the lists
    def add_student(self, student: Student):
        self.__students.append(student)

    def add_course(self, course: Course):
        self.__courses.append(course)

    # Polymorphism:
    # Common input method to input student or course data
    def input(self, entity_type):
        if entity_type == 'student':
            student = Student("", "", "", {})
            student.input()  # Call student-specific input
            self.add_student(student)
        elif entity_type == 'course':
            course = Course("", "")
            course.input()  # Call course-specific input
            self.add_course(course)

    # Enter marks for students in a specific course
    def enter_marks(self):
        course_id = input("Enter course ID to input marks: ")
        course = None
        for c in self.__courses:
            if c.get_course_id() == course_id:
                course = c
                break

        if not course:
            print("Course not found!")
            return

        print(f"Entering marks for course: {course.get_course_name()}")
        for student in self.__students:
            mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_student_id()}): "))
            student.set_marks(course_id, mark)

    # Display all students
    def list_students(self):
        if not self.__students:
            print("No students available.")
        else:
            for student in self.__students:
                print(student)

    # Display all courses
    def list_courses(self):
        if not self.__courses:
            print("No courses available.")
        else:
            for course in self.__courses:
                print(course)

    # Display marks for a specific course
    def display_marks(self):
        course_id = input("Enter the course ID to display marks: ")
        course = None
        for c in self.__courses:
            if c.get_course_id() == course_id:
                course = c
                break

        if not course:
            print("Course not found!")
            return

        print(f"Marks for course: {course.get_course_name()}")
        for student in self.__students:
            marks = student.get_marks().get(course_id, "No marks entered")
            print(f"{student.get_name()} (ID: {student.get_student_id()}): {marks}")


def main():
    school = School()

    while True:
        print("\nOptions:")
        print("0. Load pre-entered data:(If don't have data, please choose this option first)")
        print("1. Input number of students:")
        print("2. Input number of courses:")
        print("3. Input students info:")
        print("4. Input courses info:")
        print("5. Enter marks for a specific course:")
        print("6. Display all students")
        print("7. Display all courses")
        print("8. Display marks for a specific course")
        print("9. Exit\n")

        choice = int(input("Enter your choice: "))
        if choice == 0:
            pre_entered_students = [
                Student("BI14001", "Anh", "15/07/2005", {"ICT1.001": 10.3, "ICT2.004": 3.2}),
                Student("BI14002", "Huy", "22/10/2005", {"ICT1.001": 5.0}),
                Student("BI14003", "Si", "02/09/2005", {"ICT3.002": -2.0, "ICT1.001": 1.0}),
            ]
            pre_entered_courses = [
                Course("ICT1.001", "Basic Programming"),
                Course("ICT2.004", "OOP"),
                Course("ICT3.002", "Database"),
            ]
            for student in pre_entered_students:
                school.add_student(student)
            for course in pre_entered_courses:
                school.add_course(course)
            print("Successfully loaded pre-entered data.")
        elif choice == 1:
            num_students = int(input("Enter number of students: "))
            for _ in range(num_students):
                school.input('student')
        elif choice == 2:
            num_courses = int(input("Enter number of courses: "))
            for _ in range(num_courses):
                school.input('course')
        elif choice == 3:
            school.list_students()
        elif choice == 4:
            school.list_courses()
        elif choice == 5:
            school.enter_marks()
        elif choice == 6:
            school.display_marks()
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
