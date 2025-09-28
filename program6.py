# Strings
# A string is a sequence of characters, and it is one of the fundamental data types used to represent textual data.

# Single quote string
user_name = 'This is string.'
print(f"Your user name is {user_name}")

# double quote string
user_gender = "male"
print(f"User's gender is {user_gender}")

# Multiline string using triple quotes
# you can use either single quote or double qoute thrice.
user_address = """
    Mahaveer Nagar,
    123-121, Tilak Road,
    Pune, Maharashtra.
"""
# or 
user_address2 = '''
    Mahaveer Nagar,
    123-121, Tilak Road,
    Pune, Maharashtra.
'''
print(f"User's address is : {user_address}")

# Concatenation
str1 = "Hello"
str2 = ", "+"World"
print(f"Welcome message : {str1+str2}")

# String length
user_email_address = "user@gmail.com"
print(f"Length of your email is {len(user_email_address)}")

# String indexing and slicing
user_email_address = "user@gmail.com"
print(f"Character present at index 5 : {user_email_address[4]}")
user_email_name = user_email_address[0:4] # exclusive 4
print(f"Username : {user_email_name}")
user_email_name = user_email_address[:4] # exclusive 4
print(f"Username : {user_email_name}")
user_email_domain = user_email_address[5:] # inclusive last char
print(f"Domain : {user_email_domain}")
user_email_reverse = user_email_address[::-1]
print(f"Reversed email address : {user_email_reverse}")

# String methods
username = "  Sohal.jSon  "
upper_username = username.upper()
print(f"Username in uppercase : {upper_username}")
lower_username = username.lower()
print(f"Username in lowercase : {lower_username}")
stripped_username = username.strip()
print(f"Stripped user name : {stripped_username}")

# String formatting
username = "john"
age = 21
print(f"Age of {username} is {age}.")

# Escape characters
print("This is first line.\nThis is second line.\nThis is third line.")