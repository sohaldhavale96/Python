# Function parameters
# Function parameters are values that are passed into a function when it is called. They allow functions to take input, making them more veratile and adaptable.

def add(a, b): # parameters
    return a+b

print(add(a=2,b=3)) # arguments

names = ["python","javascript","cpp"]
def lets_code(code_language):
    print(f"lets code in {code_language}")

for code in names:
    lets_code(code_language=code)
