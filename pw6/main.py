import curses
from domains import School
from input import input_student, input_course
from output import display_menu

def main(stdscr):
    school = School(stdscr)

    pre_entered_students = [
        input_student(),
        input_student(),
        input_student(),
    ]
    pre_entered_courses = [
        input_course(),
        input_course(),
        input_course(),
    ]

    for student in pre_entered_students:
        school.add_student(student)

    for course in pre_entered_courses:
        school.add_course(course)

    while True:
        display_menu(stdscr)
        c = stdscr.getch()
        if c == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)