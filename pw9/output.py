import tkinter as tk
from tkinter import ttk, messagebox

def display_students(school, root):
    display_table(root, "Student List", school.get_students(), ["Student ID", "Name", "Date of Birth"], 
                  lambda student: [student.get_student_id(), student.get_name(), student.get_dob()])

def display_courses(school, root):
    display_table(root, "Course List", school.get_courses(), ["Course ID", "Name", "Credits"], 
                  lambda course: [course.get_course_id(), course.get_course_name(), course.get_credits()])

def display_marks(school, root):
    if not school.get_students():
        messagebox.showerror("Error", "No students available.")
        return
    if not school.get_courses():
        messagebox.showerror("Error", "No courses available.")
        return
    
    display_table(root, "Marks List", school.get_students(), ["Student ID", "Name", "Marks"], 
                  lambda student: [student.get_student_id(), student.get_name(), student.get_marks()])

def display_gpa(school, root):
    if not school.get_students():
        messagebox.showerror("Error", "No students available.")
        return
    avg_gpa = sum(student.calculate_gpa(school.get_courses()) for student in school.get_students()) / len(school.get_students())
    messagebox.showinfo("Average GPA", f"Average GPA: {avg_gpa:.2f}")

# Helper function for displaying tables
def display_table(root, title, items, columns, extract_values):
    table_window = tk.Toplevel(root)
    table_window.title(title)

    tree = ttk.Treeview(table_window, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

    for col in columns:
        tree.heading(col, text=col)

    for item in items:
        tree.insert("", "end", values=extract_values(item))
