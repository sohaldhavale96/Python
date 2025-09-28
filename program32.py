# Scope
# A scope refers to the region of a program where a particular variable can be accessed or modified. The scope of variable is determined by where it is defined in the code, and it plays crucial role in understanding how variables are accessed and manipulated within a program. 

# Global Scope
# Variables defined at th etop level are considered to be a global.
# Global variables can be accessed and modified from any part of the code, including within a function.

gloabl_variable = 10

def print_gloabl_variable():
    print("Global variable : ", gloabl_variable)

print_gloabl_variable()


# Local Scope
# Variables are defined within a function have local scope and are only accessible within that function. 
# Once the function execution is completed, local variables are typically destroyed and their values are no longer accessible.

def my_function():
    local_variable = 12
    print("Print local variable : ",local_variable)

my_function() # prints local variable
print(local_variable) # error : NameError: name 'local_variable' is not defined.