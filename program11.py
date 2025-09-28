# Logical Operators
# Logical operators are used to perform logical operations on boolean values. These operations allows you to combine or modify boolean values and make more complex decisions in your code.

# and : true if both are true
# or : true if atleast one is true
# not : flip the boolean value

# Desclaimer : Below code is just for illustration purpose
original_user_name = "admin"
original_password = "admin@2025"

user_name = input("Enter your username : ")
password = input("Enter your password : ")
if (user_name==original_user_name and original_password==password):
    print(f"Login success!")
elif user_name==original_user_name and original_password!=password: 
    print(f"password incorrect") # Not recommended in production level
elif user_name!=original_user_name and original_password==password:
    print(f"Username is incorrect.") # Not exists and not recommended in production level
else:
    print(f"Invalid credentials! Please enter valid credentials!")