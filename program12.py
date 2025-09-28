# Conditional statements
# Conditional statements are used to control the flow of program based on certain conditions. They allow you to execute different blocks of code depending on whether a specified condition evaluates to True or False.

# if
age = 14
if age<18:
    print(f"User must have age above 18!")

# if-else
age = 21
if age<18:
    print(f"User must have age above 18 or equal to 18!")
else:
    print(f"U are adult!")

# elif
age = 18
if age<18:
    print(f"User must have age equal to 18!")
elif age>18:
    print(f"User must have age equal to 18!")
else:
    print(f"User is 18!")
