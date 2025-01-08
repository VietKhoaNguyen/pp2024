import tkinter as tk
from domain import School # type: ignore
from input import add_student_form, add_course_form
from output import display_students, display_courses, display_marks, display_gpa

def main():
    root = tk.Tk()
    root.title("University Management System")
    school = School(None)

    # Main Menu
    tk.Label(root, text="University Management System", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Add Student", command=lambda: add_student_form(school, root)).pack(pady=5)
    tk.Button(root, text="Add Course", command=lambda: add_course_form(school, root)).pack(pady=5)
    tk.Button(root, text="Display Students", command=lambda: display_students(school, root)).pack(pady=5)
    tk.Button(root, text="Display Courses", command=lambda: display_courses(school, root)).pack(pady=5)
    tk.Button(root, text="Display Marks", command=lambda: display_marks(school, root)).pack(pady=5)
    tk.Button(root, text="Display GPA", command=lambda: display_gpa(school, root)).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
