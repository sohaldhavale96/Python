# Static variable
# A static variable (or a class variable) that belongs to the class itself rather than to instances of the class. This means that the variable is shared among ll instances of the class. Static variables are defined inside a class but outside any methods, typically at the beginning of the class defination.

class Student():
    # static variable
    number_of_students = 0

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.number_of_students += 1

student1 = Student("Json", 21)
student2 = Student("John", 21)
print("number of students enrolled : ",Student.number_of_students)

