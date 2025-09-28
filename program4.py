# Input function
# input() function is used to take input from the user during the execution of the program. The input() function reads a line of text from the user as a "string". It allows the user to provide input interactively.

# Getting input from user
user_name = input("Enter your name :")
print("Your name is",user_name)

user_age = int(input("Enter your age :"))
print("Your age is",user_age)

user_cgpa = float(input("Enter your CGPA:"))
percentage = user_cgpa * 10
print(f"Your percentage is",percentage)