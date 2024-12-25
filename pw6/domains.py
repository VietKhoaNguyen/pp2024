import pickle
import gzip

class Person:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def input(self):
        self.__name = input("Enter name: ")
        self.__dob = input("Enter Date of Birth (DD/MM/YYYY): ")

    def __str__(self):
        return f"Name: {self.__name}, DoB: {self.__dob}"

class Course:
    def __init__(self, course_id, course_name, credits):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credits = credits

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_credits(self):
        return self.__credits

    def input(self):
        self.__course_id = input("Enter course ID: ")
        self.__course_name = input("Enter course name: ")
        self.__credits = float(input("Enter course credits: "))

    def __str__(self):
        return f"CourseID: {self.__course_id}, Name: {self.__course_name}, Credits: {self.__credits}"

class Student(Person):
    def __init__(self, student_id, name, dob, marks=None):
        super().__init__(name, dob)
        self.__student_id = student_id
        self.__marks = marks if marks is not None else {}

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, course_id, mark):
        self.__marks[course_id] = mark

    def calculate_gpa(self, courses):
        total_credits = 0
        total_weighted_marks = 0
        for course_id, mark in self.__marks.items():
            for course in courses:
                if course.get_course_id() == course_id:
                    total_credits += course.get_credits()
                    total_weighted_marks += mark * course.get_credits()
                    break
        return total_weighted_marks / total_credits if total_credits != 0 else 0

    def __str__(self):
        return f"StudentID: {self.__student_id}, {super().__str__()}, Marks: {self.__marks}"

class School:
    def __init__(self, stdscr):
        self.__students = self.load_data("students.pkl.gz") or []
        self.__courses = self.load_data("courses.pkl.gz") or []
        self.stdscr = stdscr

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def add_student(self, student):
        self.__students.append(student)
        self.save_data("students.pkl.gz", self.__students)

    def add_course(self, course):
        self.__courses.append(course)
        self.save_data("courses.pkl.gz", self.__courses)

    def enter_marks(self):
        for course in self.__courses:
            course_id = course.get_course_id()
            for student in self.__students:
                try:
                    mark = float(input(f"Enter mark for student {student.get_name()} in {course.get_course_name()} (ID: {student.get_student_id()}): "))
                    student.set_marks(course_id, mark)
                except ValueError:
                    print("Invalid mark entered. Skipping.")
                    continue
        self.save_data("marks.pkl.gz", self.__students)

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda student: student.calculate_gpa(self.__courses), reverse=True)

    @staticmethod
    def save_data(file_name, data):
        with gzip.open(file_name, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def load_data(file_name):
        try:
            with gzip.open(file_name, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return None