import curses
from domains import School
from input import input_student, input_course
from output import display_menu

def main(stdscr):
    school = School(stdscr)

    while True:
        display_menu(stdscr)
        c = stdscr.getch()

        if c == ord('1'):
            student = input_student()
            school.add_student(student)
        elif c == ord('2'):
            course = input_course()
            school.add_course(course)
        elif c == ord('3'):
            school.enter_marks()
        elif c == ord('4'):
            # Implement display marks logic if needed
            pass
        elif c == ord('5'):
            # Implement average GPA display if needed
            pass
        elif c == ord('6'):
            school.sort_students_by_gpa()
        elif c == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)