import tkinter as tk
from tkinter import messagebox
from domain import Student, Course # type: ignore

def add_student_form(school, root):
    def save_student():
        try:
            student_id = student_id_entry.get()
            name = name_entry.get()
            dob = dob_entry.get()
            if not student_id or not name or not dob:
                raise ValueError("All fields are required.")
            
            student = Student(student_id, name, dob)
            school.add_student(student)
            messagebox.showinfo("Success", "Student added successfully!")
            form.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    form = create_form(root, "Add Student", save_student)
    student_id_entry = add_input_field(form, "Student ID:")
    name_entry = add_input_field(form, "Name:")
    dob_entry = add_input_field(form, "Date of Birth (DD/MM/YYYY):")

def add_course_form(school, root):
    def save_course():
        try:
            course_id = course_id_entry.get()
            course_name = course_name_entry.get()
            credits = float(credits_entry.get())
            if not course_id or not course_name or credits <= 0:
                raise ValueError("All fields are required and credits must be positive.")
            
            course = Course(course_id, course_name, credits)
            school.add_course(course)
            messagebox.showinfo("Success", "Course added successfully!")
            form.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    form = create_form(root, "Add Course", save_course)
    course_id_entry = add_input_field(form, "Course ID:")
    course_name_entry = add_input_field(form, "Course Name:")
    credits_entry = add_input_field(form, "Credits:")

# Helper functions for creating forms
def create_form(root, title, save_callback):
    form = tk.Toplevel(root)
    form.title(title)
    form.geometry("400x300")
    tk.Button(form, text="Save", command=save_callback).pack(pady=10)
    return form

def add_input_field(form, label_text):
    tk.Label(form, text=label_text).pack()
    entry = tk.Entry(form)
    entry.pack(pady=5)
    return entry
