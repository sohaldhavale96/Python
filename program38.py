# OOP
# Object Oriented Programming is a programming paradigm that organizes code into objects, which are instances of classes. It is a way of structuring and designing code to model real-world entities and their interactions.

# Inheritance
# super class
class Animal():
    def __init__(self):
        self.legs = 4
    
class Dog(Animal):
    def bark(self):
        print(f"Dog is barking.")
    def run(self):
        print(f"Dog is running.")
    
dog = Dog()
dog.run()
print(f"Dog has {dog.legs} legs.")