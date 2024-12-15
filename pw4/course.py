# pw4/course.py
class Course:
    def __init__(self, course_id, course_name, credits):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credits = credits

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_credits(self):
        return self.__credits

    def input(self):
        self.__course_id = input("Enter course ID: ")
        self.__course_name = input("Enter course name: ")
        self.__credits = float(input("Enter course credits: "))

    def __str__(self):
        return f"CourseID: {self.__course_id}, Name: {self.__course_name}, Credits: {self.__credits}"
