import numpy as np
import math
import curses


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

    def input(self):
        super().input()
        self.__student_id = input("Enter student ID: ")

    def calculate_gpa(self, courses):
        # Calculate GPA as a weighted sum of marks and course credits
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
        self.__students = []
        self.__courses = []
        self.stdscr = stdscr  # for curses UI

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def input(self, entity_type):
        if entity_type == 'student':
            student = Student("", "", "", {})
            student.input()
            self.add_student(student)
        elif entity_type == 'course':
            course = Course("", "", 0)
            course.input()
            self.add_course(course)

    def enter_marks(self):
        for course in self.__courses:
            course_id = course.get_course_id()
            for student in self.__students:
                try:
                    mark = float(input(f"Enter mark for student {student.get_name()} in {course.get_course_name()} (ID: {student.get_student_id()}): "))
                    mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
                    student.set_marks(course_id, mark)
                except ValueError:
                    print("Invalid mark entered. Skipping.")
                    continue

    def display_marks(self):
        for course in self.__courses:
            print(f"Marks for course: {course.get_course_name()}")
            for student in self.__students:
                mark = student.get_marks().get(course.get_course_id(), "No mark entered")
                print(f"{student.get_name()} (ID: {student.get_student_id()}): {mark}")

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda student: student.calculate_gpa(self.__courses), reverse=True)

    def list_students(self):
        for student in self.__students:
            print(student)

    def list_courses(self):
        for course in self.__courses:
            print(course)

    def calculate_and_display_average_gpa(self):
        for student in self.__students:
            gpa = student.calculate_gpa(self.__courses)
            print(f"{student.get_name()} (ID: {student.get_student_id()}) GPA: {gpa:.2f}")

    # Curses UI
    def show_ui(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "University Management System")
        self.stdscr.addstr(1, 0, "1. Enter students info")
        self.stdscr.addstr(2, 0, "2. Enter courses info")
        self.stdscr.addstr(3, 0, "3. Enter marks for students")
        self.stdscr.addstr(4, 0, "4. Display marks")
        self.stdscr.addstr(5, 0, "5. Display average GPA")
        self.stdscr.addstr(6, 0, "6. Sort students by GPA")
        self.stdscr.addstr(7, 0, "Press q to quit")

        self.stdscr.refresh()

        while True:
            c = self.stdscr.getch()

            if c == ord('1'):
                self.input('student')
            elif c == ord('2'):
                self.input('course')
            elif c == ord('3'):
                self.enter_marks()
            elif c == ord('4'):
                self.display_marks()
            elif c == ord('5'):
                self.calculate_and_display_average_gpa()
            elif c == ord('6'):
                self.sort_students_by_gpa()
                self.list_students()
            elif c == ord('q'):
                break

            self.stdscr.clear()
            self.show_ui()


def main(stdscr):
    school = School(stdscr)

    pre_entered_students = [
        Student("BI14001", "Anh", "15/07/2005", {"ICT1.001": 10.3, "ICT2.004": 3.2}),
        Student("BI14002", "Huy", "22/10/2005", {"ICT1.001": 5.0}),
        Student("BI14003", "Si", "02/09/2005", {"ICT3.002": -2.0, "ICT1.001": 1.0}),
    ]
    pre_entered_courses = [
        Course("ICT1.001", "Basic Programming", 3),
        Course("ICT2.004", "OOP", 4),
        Course("ICT3.002", "Database", 3),
    ]

    for student in pre_entered_students:
        school.add_student(student)

    for course in pre_entered_courses:
        school.add_course(course)

    school.show_ui()


if __name__ == "__main__":
    curses.wrapper(main)
