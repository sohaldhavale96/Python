# Functions
# A function is a block of reusable code that perform a specific task or set of tasks, we can define a function by using the "def" keyword.

# defining function
def greet():
    print("Hello Python!")
# calling/ invoking/ executing function
greet()
greet()


# addition of two numbers
def add(a,b)->int:
    return a+b
result = add(12,13)
print("Result of adding 12 and 13 :",result)