class Person:
    def __init__(self,name,dob):
        self.__name = name
        self.__dob = dob
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
class Stu(Person):  # Inherit from Person class
    def __init__(self, id, name, dob, marks={}):
        super().__init__(name, dob)  # Call the Person's constructor
        self.__id = id
        self.__marks = marks
        
    def get_id(self):
        return self.__id

    def get_marks(self):
        return self.__marks
    
    def fill_mark(self, course_id, point):
        self.__marks[course_id] = point

    # Display string
    def __str__(self):
        return f"StudentID: {self.get_id()}, Name: {self.get_name()}, DoB: {self.get_dob()}"

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    # Display string
    def __str__(self):
        return f"CourseID: {self.get_id()}, Name: {self.get_name()}"

class Outils:
    def show(list):
        for instance in list:
            print(instance)

    def input_Integer(args) -> int:
        return int(input(f"Enter the number of {args}: "))

class School:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []

    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    def set_students(self, num):
        self.__num_students = num

    def set_courses(self, num):
        self.__num_courses = num    

    def set_num_students(self):
        self.__num_students = Outils.input_Integer("students")

    def set_num_courses(self):
        self.__num_courses = Outils.input_Integer("courses")

    def add_student(self):
        id = input("Enter the student's id: ")
        name = input("Enter the student's name: ")
        dob = input("Enter the student's dob: ")  
        self.__students.append(Stu(id,name,dob))
    
    def add_course(self):
        id = input("Enter the course's id: ")
        name = input("Enter the course's name: ")
        self.__courses.append(Course(id,name))

    def input_students(self):
        if self.get_num_students() == 0:
            print("Please input the number of students first")  
        for _ in range(self.get_num_students()):
            self.add_student()

    def input_courses(self):
        if self.get_num_courses() == 0:
            print("Please input the number of courses first")
        for _ in range(self.get_num_courses()):
            self.add_course()

    def load_courses(self, courses):
        self.__courses = courses

    def load_students(self, students):
        self.__students = students

    def enter_mark(self):
        course_id = input("Enter the course ID to input marks: ")
        course = None

        for c in self.__courses:
            if c.get_id() == course_id:
                course = c
                break
        
        if course is None:
            print("Course not found!")
            return
        
        print(f"Entering marks for course: {course.get_name()}")
        for student in self.__students:
            mark = float(input(f"Enter marks for student {student.get_name()} (ID: {student.get_id()}): "))
            student.get_marks()[course_id] = mark

    def display_mark(self):
        course_id = input("Enter the course ID to view marks: ")
    
        course = None
        for c in self.__courses:
            if c.get_id() == course_id:
                course = c
                break

        if course is None:
            print("Course not found!")
            return
        print(f"Marks for course: {course.get_name()}")

        for student in self.__students:
            if course_id in student.get_marks():
                print(f"Student {student.get_name()} (ID: {student.get_id()}): {student.get_marks()[course_id]}")
            else:
                print(f"Student {student.get_name()} (ID: {student.get_id()}): No marks entered")

    def list_students(self):
        if not self.get_students():
            print("No students input yet")
            return
        
        print("Student list:")
        Outils.show(self.get_students())

    def list_courses(self):
        if not self.get_courses():
            print("No courses input yet")
            return

        print("Course list: ")
        Outils.show(self.get_courses())

def main():
    Uni = School()

    while True:
        print("\nOptions:")
        print("0. Load pre-entered data:(If don't have data, please choose this option first)")
        print("1. Input number of students:")
        print("2. Input number of courses:")
        print("3. Input students info:")
        print("4. Input courses info:")
        print("5. Enter mark of students in a specific course:")
        print("6. Display all students")
        print("7. Display all courses")
        print("8. Display mark for a specific course")
        print("9. Exit\n")   

        choice = int(input("Enter your choice: "))
        if choice == 0:
            pre_entered_students: list[Stu] = [
                Stu("BI14001", "Anh", "15/07/2005", {"ICT1.001": 10.3, "ICT2.004": 3.2}),
                Stu("BI14002", "Huy", "22/10/2005", {"ICT1.001": 5.0}),
                Stu("BI14003", "Si", "02/09/2005", {"ICT3.002": -2.0, "ICT1.001": 1.0})
            ]

            pre_entered_courses: list[Course] = [
                Course("ICT1.001", "Basic Programming"),
                Course("ICT2.004", "OOP"),
                Course("ICT3.002", "Database")
            ]
            Uni.set_courses(len(pre_entered_courses))
            Uni.set_students(len(pre_entered_students))
            Uni.load_courses(pre_entered_courses)
            Uni.load_students(pre_entered_students)
            print("Successfully loaded pre-entered data.")
        elif choice == 1:
            Uni.set_num_students()
        elif choice == 2:
            Uni.set_num_courses()
        elif choice == 3:
            Uni.input_students()
        elif choice == 4:
            Uni.input_courses()
        elif choice == 5:
            Uni.enter_mark()
        elif choice == 6:
            Uni.list_students()
        elif choice == 7:
            Uni.list_courses()
        elif choice == 8:
            Uni.display_mark()
        elif choice == 9:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
