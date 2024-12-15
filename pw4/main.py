# pw4/main.py
import curses
from pw4.school import School
from pw4.student import Student
from pw4.course import Course

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
    