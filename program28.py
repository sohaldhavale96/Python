# Named arguments
# Keywords arguements, aka named arguments, allow you to pass value to a function by explicityly specifying the parameter names along with their values. This can make function calls more readable and allow you to provide arguments in a different order than they appear in the function defination.

def display_info(name="user", age=18, city="city"):
    print(f"Hi. My name is {name}. My age is {age}. I live in {city}.")

display_info(name="json",age=21,city="kop")
display_info(age=21)