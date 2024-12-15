# pw4/school.py
import math
from pw4.student import Student
from pw4.course import Course

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
