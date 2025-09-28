# Type Casting
# type casting refers to the process of converting one data type into another. Python provides several built-in functions for type-casting, allowing you to convert variables from one type to another.

# int()
age = "21"
int_age = int(age)
print(f"type of age : {type(age)}, type of int_age : {type(int_age)}")
cgpa = 8.40
int_cgpa = int(cgpa)
print(f"type of cgpa : {type(cgpa)}, type of int_cgpa : {type(int_cgpa)}")

# float()
cgpa = "8.40"
float_cgpa = float(cgpa)
print(f"type of cgpa : {type(cgpa)}, type of float_cgpa : {type(float_cgpa)}")
temperature = 33
float_temperature = float(temperature)
print(f"type of temperature : {type(temperature)}, type of float_temp : {type(float_temperature)}")

# str()
temperature = 33.2421
str_temperature = str(temperature)
print(f"type of temperature : {type(temperature)}, type of str_temperature : {type(str_temperature )}")

# bool
result = 12
bool_result = bool(result)
print(f"type of result : {type(result)}, type of bool_result : {type(bool_result)} : {bool_result}")
response = 0
bool_response = bool(response)
print(f"type of response : {type(response)}, type of bool_response : {type(bool_response)}")