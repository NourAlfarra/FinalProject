class Course:
    num_courses = 0

    def __init__(self, name, level):
        Course.num_courses += 1
        self.course_id = Course.num_courses
        self.name = name
        self.level = level

    def get_course_id(self):
        return self.course_id

    def get_course_level(self):
        return self.level


class Student:
    num_students = 0

    def __init__(self, name, level):
        Student.num_students += 1
        self.student_id = Student.num_students
        self.name = name
        self.level = level
        self.courses = []

    def add_course(self, course):
        if course.get_course_level() == self.level:
            self.courses.append(course)
            print("Course added successfully.")
        else:
            print("Error: Course level does not match student level.")

    def display_details(self):
        print("Name: ", self.name)
        print("Level: ", self.level)
        print("Courses Enrolled:")
        for course in self.courses:
            print("- ", course.name)

    def get_student_id(self):
        return self.student_id



students = []
courses = []



def find_student_by_id(student_id):
    for student in students:
        if student.get_student_id() == student_id:
            return student
    return None



def find_course_by_id(course_id):
    for course in courses:
        if course.get_course_id() == course_id:
            return course
    return None



def add_new_student():
    name = input("Enter student name: ")
    level = input("Enter student level (A, B, or C): ")
    while level not in ["A", "B", "C"]:
        level = input("Invalid input. Please enter student level (A, B, or C): ")
    student = Student(name, level)
    students.append(student)
    print("Student saved successfully.")



def remove_student():
    student_id = int(input("Enter student ID: "))
    student = find_student_by_id(student_id)
    if student:
        students.remove(student)
        print("Delete done successfully.")
    else:
        print("User not exist.")



def edit_student():
    student_id = int(input("Enter student ID: "))
    student = find_student_by_id(student_id)
    if student:
        name = input("Enter new name: ")
        level = input("Enter new level (A, B, or C): ")
        while level not in ["A", "B", "C"]:
            level = input("Invalid input. Please enter student level (A, B, or C): ")
        student.name = name
        student.level = level
    else:
        print("User not exist.")



def display_all_students():
    print("All Students:")
    for student in students:
        student.display_details()


def add_new_course():
    name = input("Enter course name: ")
    level = input("Enter course level (A, B, or C): ")
    while level not in ["A", "B", "C"]:
        level = input("Invalid input. Please enter course level (A, B, or C): ")
    course = Course(name, level)
    courses.append(course)
    print("Course saved successfully.")



def add_course_to_student():
     student_id = int(input("Enter student ID: "))
     student = find_student_by_id(student_id)
     if student:
        course_id = int(input("Enter course ID: "))
        course = find_course_by_id(course_id)
        if course:
            student.add_course(course)
        else:
            print("Course not exist.")
     else:
        print("User not exist.")

x1 = 10
while x1 != 0:
 print("Select Choice Please")
 print("1.Add New Student")
 print("2.Remove Student")
 print("3.Edit Student")
 print("4.Display All Student")
 print("5.Create New Course")
 print("6.Add New course to student")
 print("0.Exit")
 x1 = int(input("Enter the Number of operation"))
 if x1 == 1:
     add_new_student()
 elif x1 == 2:
     remove_student()
 elif x1 == 3:
     edit_student()
 elif x1 == 4:
     display_all_students()
 elif x1 == 5:
     add_new_course()
 elif x1 == 6:
     add_course_to_student()
 elif x1 == 0:
    print("Thank you")
