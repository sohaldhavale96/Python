# Variable
# a variable is a symbolic name that is used to store and represent data values. It is essentially a label or identifier for a memory location where a values is stored.

age = int(22)
print(type(age))
print(age)
print(f"My age is {age}")
print("my age is",age)

# Identifier
# Identifier is a name given to entities like variables, functions, classes, modules etc. It helps to uniquely identify these entities in program.

# Rule for Identifier 
# It must start with a-z, A-Z or an underscore(_).
# The remaining characters can be letters, underscore, or digits(0-9).
# Python is case sensitive, so Variable and variable is different.
# reserved keywords are not allowed.

# Conventions for naming identifiers
# Use descriptive names to make code more readable
# Avoid using names that are too short and too cryptic.
# Use underscore to seperate words in multi-word identifier(snake_case). ex. is_passed 
# for constants, use all capital letters with underscore seperating words(UPPER_CASE) ex.MAX_SIZE