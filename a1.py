# Class Student (complete activity 1, DSCM2L3). Python 3 standard library only.
# Run: python class_student.py  (or paste into one Google Colab cell and press Run)


# A: the class keyword makes a blueprint called Student.
class Student:
    # B: this print is in the class body. Python runs the body ONCE, when it reads
    # the class, not each time an object is made. Count how often you see this line.
    print("Python read the Student blueprint.")
    school = "Sunrise School"        # C: a class variable, shared by every Student
    # Step 1: Add a class variable
    grade = 10
    print("Class variable grade:", grade)


# Step 2: Make two objects
anna = Student()
ryan = Student()
print("anna is a", type(anna))                                 # D

# Step 3: Read shared class variables
print("anna's school:", anna.school, "| ryan's grade:", ryan.grade)
new_grade = int(input("New class grade? "))
Student.grade = new_grade
print("After changing the class grade: anna", anna.grade, "| ryan", ryan.grade)

# Step 4: Edge case: give one object its own value
anna.grade = 12
print("anna", anna.grade, "| ryan", ryan.grade, "| Student", Student.grade)
