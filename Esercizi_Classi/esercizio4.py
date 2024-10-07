# Exercise 4: University Management System
# Create a system to manage a university with departments, courses, professors, and students. 
# Create an abstract class Person:
# Attributes:
# name (string)
# age (int)
# Methods:
# __init__ method to initialize the attributes.
# Abstract method get_role to be implemented by subclasses.
# __str__ method to return a string representation of the person.
# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:
# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.
# Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.
# Create a class Course:
# Attributes:
# course_name (string)
# course_code (string)
# students (list of Student instances)
# professor (Professor instance)
# Methods:
# __init__ method to initialize the attributes.
# add_student(student) to add a student to the course.
# set_professor(professor) to set the professor for the course.
# __str__ method to return a string representation of the course.
# Create a class Department:
# Attributes:
# department_name (string)
# courses (list of Course instances)
# professors (list of Professor instances)
# Methods:
# __init__ method to initialize the attributes.
# add_course(course) to add a course to the department.
# add_professor(professor) to add a professor to the department.
# __str__ method to return a string representation of the department.
# Create a class University:
# Attributes:
# name (string)
# departments (list of Department instances)
# students (list of Student instances)
# Methods:
# __init__ method to initialize the attributes.
# add_department(department) to add a department to the university.
# add_student(student) to add a student to the university.
# __str__ method to return a string representation of the university.
# Create a script:
# Create instances of departments, courses, professors, and students.
# Add them to the university.
# Enroll students in courses and assign professors to courses.
# Display the state of the university.
from abc import abstractmethod

class Person:
    def __init__(self,name:str,age :int) -> None:
        self.name = name
        self.age = age
    @abstractmethod  
    def get_role(self):
        pass
        
    def __str__(self) -> str:
        return f'name : {self.name} , age : {self.age}'

class Student(Person):
    def __init__(self, name: str, age: int,student_id :str) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
        
        
    def get_role(self):
        return "Student"
        
    def enroll(self,course):
        self.courses.append(course)
        course.add_students(self.name)

class Professor(Person):
    def __init__(self, name: str, age: int,professor_id :str,department:str) -> None:
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses = []
        
    def get_role(self):
        return "Professor"
        
    def assign_to_course(self, course):
        self.courses.append(course)
        course.set_professor(self.name)

    
class Course:
    def __init__(self,course_name:str,course_code:str,professor:Professor) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.professor:Professor = professor
        self.students :list[Student] = []
    
    def add_students(self,student:Student):
        return self.students.append(student)
    
    def set_professor(self,professor:Professor):
        self.professor = professor
        
    def __str__(self) -> str:
        return f'course name :{self.course_name}, course code : {self.course_code}, professor : {self.professor}, students : {self.students}'
        
class Department:
    def __init__(self,
                 department_name: str) -> None:
        self.department_name = department_name
        self.courses :list[Course]= []
        self.professors :list[Professor]= []

    def add_course(self, course: Course):
        self.courses.append(course)

    def add_professor(self, professor: Professor):
        self.professors.append(professor)

    def __str__(self) -> str:
        return f'Department name :{self.department_name}, courses : {self.courses}, professors : {self.professors}'

class University:
    def __init__(self,name: str) -> None:
        self.name = name
        self.departments :list[Department] = []
        self.students :list[Student]= []

    def add_department(self, department: Department):
        self.departments.append(department)

    def add_student(self, student: Student):
        self.students.append(student)

    def __str__(self) -> str:
         return f'University name :{self.name}, departments : {self.departments}, students : {self.students}'
     
     
     
cs_department = Department("Computer Science")
math_department = Department("Mathematics")

prof1 = Professor("Dr. Alice", 45, "P001", "Computer Science")
prof2 = Professor("Dr. Bob", 50, "P002", "Mathematics")
prof3 = Professor("Dr. Lorenzo", 44, "P003", "Python")

student1 = Student("John Doe", 20, "S001")
student2 = Student("Jane Smith", 22, "S002")

course1 = Course("Algorithms", "CS101",prof1)
course2 = Course("Data Structures", "CS102",prof2)
course3 = Course("Calculus", "MATH101",prof3)



university = University("XYZ University")
university.add_department(cs_department)
university.add_department(math_department)
university.add_student(student1)
university.add_student(student2)

cs_department.add_course(course1)
cs_department.add_course(course2)
math_department.add_course(course3)

cs_department.add_professor(prof1)
math_department.add_professor(prof2)
math_department.add_professor(prof3)


student1.enroll(course1)
student2.enroll(course2)
student1.enroll(course3)

prof1.assign_to_course(course1)
prof3.assign_to_course(course2)
prof2.assign_to_course(course3)
print(course1)
print(course2)
print(course3)
print(cs_department)
print(math_department)
print(university)