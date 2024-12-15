# pw4/student.py
import math
from pw4.person import Person
from pw4.course import Course

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
