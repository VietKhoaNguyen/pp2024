import curses
from domain import School # type: ignore
from input import input_student, input_course
from output import display_menu, display_marks, display_average_gpa, display_sorted_students

def main(stdscr):
    school = School(stdscr)

    while True:
        display_menu(stdscr)
        c = stdscr.getch()

        if c == ord('1'):  # Add Student
            student = input_student()
            school.add_student(student)

        elif c == ord('2'):  # Add Course
            course = input_course()
            school.add_course(course)

        elif c == ord('3'):  # Enter Marks
            if not school.get_students() or not school.get_courses():
                stdscr.clear()
                stdscr.addstr(0, 0, "No students or courses available. Add them first.")
                stdscr.addstr(2, 0, "Press any key to return to the main menu.")
                stdscr.refresh()
                stdscr.getch()
            else:
                school.enter_marks()

        elif c == ord('4'):  # Display Marks
            if not school.get_students() or not school.get_courses():
                stdscr.clear()
                stdscr.addstr(0, 0, "No students or courses available. Add them first.")
                stdscr.addstr(2, 0, "Press any key to return to the main menu.")
                stdscr.refresh()
                stdscr.getch()
            else:
                display_marks(stdscr, school.get_students(), school.get_courses())

        elif c == ord('5'):  # Display Average GPA
            if not school.get_students() or not school.get_courses():
                stdscr.clear()
                stdscr.addstr(0, 0, "No students or courses available. Add them first.")
                stdscr.addstr(2, 0, "Press any key to return to the main menu.")
                stdscr.refresh()
                stdscr.getch()
            else:
                display_average_gpa(stdscr, school.get_students(), school.get_courses())

        elif c == ord('6'):  # Sort Students by GPA
            if not school.get_students() or not school.get_courses():
                stdscr.clear()
                stdscr.addstr(0, 0, "No students or courses available. Add them first.")
                stdscr.addstr(2, 0, "Press any key to return to the main menu.")
                stdscr.refresh()
                stdscr.getch()
            else:
                school.sort_students_by_gpa()
                display_sorted_students(stdscr, school.get_students(), school.get_courses())

        elif c == ord('q'):  # Quit
            break

if __name__ == "__main__":
    curses.wrapper(main)
