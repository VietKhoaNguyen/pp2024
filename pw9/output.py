import curses

def display_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "University Management System")
    stdscr.addstr(1, 0, "1. Enter students info")
    stdscr.addstr(2, 0, "2. Enter courses info")
    stdscr.addstr(3, 0, "3. Enter marks for students")
    stdscr.addstr(4, 0, "4. Display marks")
    stdscr.addstr(5, 0, "5. Display average GPA")
    stdscr.addstr(6, 0, "6. Sort students by GPA")
    stdscr.addstr(7, 0, "Press q to quit")
    stdscr.refresh()

def display_marks(stdscr, students, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "Student Marks\n")
    row = 2

    for student in students:
        stdscr.addstr(row, 0, f"Student: {student.get_name()} (ID: {student.get_student_id()})")
        row += 1
        for course_id, mark in student.get_marks().items():
            course_name = next((course.get_course_name() for course in courses if course.get_course_id() == course_id), "Unknown Course")
            stdscr.addstr(row, 4, f"{course_name}: {mark}")
            row += 1
        row += 1

    stdscr.addstr(row, 0, "Press any key to return to the main menu.")
    stdscr.refresh()
    stdscr.getch()

def display_average_gpa(stdscr, students, courses):
    stdscr.clear()
    if not students:
        stdscr.addstr(0, 0, "No students available.")
    else:
        total_gpa = sum(student.calculate_gpa(courses) for student in students)
        avg_gpa = total_gpa / len(students)
        stdscr.addstr(0, 0, f"Average GPA: {avg_gpa:.2f}")

    stdscr.addstr(2, 0, "Press any key to return to the main menu.")
    stdscr.refresh()
    stdscr.getch()

def display_sorted_students(stdscr, students, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "Students Sorted by GPA:\n")
    row = 2
    for student in students:
        gpa = student.calculate_gpa(courses)
        stdscr.addstr(row, 0, f"{student.get_name()} (ID: {student.get_student_id()}), GPA: {gpa:.2f}")
        row += 1
    stdscr.addstr(row + 1, 0, "Press any key to return to the main menu.")
    stdscr.refresh()
    stdscr.getch()
