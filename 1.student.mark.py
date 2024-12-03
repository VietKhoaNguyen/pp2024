# Add students -> class
def Num_stu(): # Number of students
    try:
        num = int(input("Num of stu/class "))
        print("Num_stu choose: %d" %num)
        return num
    except ValueError:
        print("Wrong, choose again")
        return Num_stu()

# Add student info
def Stu_info(stu): #Infomation of students
    stu_Id = input("Stu-Id: ")
    name = input("Name: ")
    dob = input("DOB: ")
    if stu_Id in stu:
        print("Exist -> Wrong")
    else:
        stu[stu_Id] = {"name": name, "dob": dob, "marks": {}}
        print("Student %s (Id: %s)" % (name, stu_Id))

# Add Num-courses
def Courses(): #Number of courses
    try:
        num = int(input("Num_cs: "))
        print("Num_c choose: %d" % num)
        return num
    except ValueError:
        print("Wrong, choose again")
        return Courses()

# Add course info
def Course_info(courses): #Infomation of courses
    c_Id = input("C-Id: ")
    name = input("C-Name: ")
    if c_Id in courses:
        print("Exists -> Wrong")
    else:
        courses[c_Id] = name
        print("Course %s (Id: %s)" % (name, c_Id))

# Add marks/course
def Mark_c(stu, courses): # Marks for each courses
    c_Id = input("C-Id: ")
    if c_Id not in courses:
        print("C-Id not found.") # Course
    else:
        print("Marks: %s (Id: %s)" % (courses[c_Id], c_Id))
        for stu_Id, stu in stu.items():
            try:
                mark = float(input("Mark %s (Id: %s): " % (stu['name'], stu_Id)))
                stu["marks"][c_Id] = mark
                print("Mark of %s" % stu['name'])
            except ValueError:
                print("Wrong, choose again")

# List courses
def list_c(courses):
    if not courses:
        print("Unavailable") # not exist
    else:
        print("\nCourses:")
        for c_Id, name in courses.items():
            print("%s: %s" % (c_Id, name))

#List students
def list_stu(stu):
    if not stu:
        print("Unavailable.") # not exist
    else:
        print("\nStudents:")
        for stu_Id, data in stu.items():
            print("Id: %s, Name: %s, DoB: %s" % (stu_Id, data['name'], data['dob']))

# stu-marks/course
def stu_mark_c(stu, courses):
    c_Id = input("C-Id: ")
    if c_Id not in courses:
        print("Unavailable.") # Course not found
    else:
        print("\nMarks for %s (Id: %s):" % (courses[c_Id], c_Id))
        for stu_Id, stu in stu.items():
            mark = stu["marks"].get(c_Id, None)
            if mark is not None:
                print("%s (Id: %s): %s" % (stu['name'], stu_Id, mark))
            else:
                print("%s (Id: %s): Unavailable." % (stu['name'], stu_Id))

# Menu
def menu():
    print(""" 
          1. Number of students:
          2. Student information: 
          3. Number of courses:
          4. Course information: 
          5. Add marks for students/courses: 
          6. List courses:
          7. List students:
          8. Show student marks/course:
          9. Exit.""")

def main():
    stu = {}
    courses = {}
    while True: # loop until exit
        menu()
        choice = input("\nChoose an option: ")
        if choice == "1":
            Num_stu()
        elif choice == "2":
            Stu_info(stu)
        elif choice == "3":
            Courses()
        elif choice == "4":
            Course_info(courses)
        elif choice == "5":
            Mark_c(stu, courses)
        elif choice == "6":
            list_c(courses)
        elif choice == "7":
            list_stu(stu)
        elif choice == "8":
           stu_mark_c(stu, courses)
        elif choice == "9":
            print("Exit.")
            break
        else:
            print("Wrong, choose again")

if __name__ == "__main__":
    main()
