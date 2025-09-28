# Class 
# A class is a blueprint for creating objects that have attributes and methods. It acts as a template for creating objects with similar characteristics.

# sample class
class Person():
    # creating functions
    # A function should atleast accept 1 parameter, i.e. self
    def talk(self):
        print("Person is talking.")

person1 = Person()
person1.talk()