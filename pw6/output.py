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