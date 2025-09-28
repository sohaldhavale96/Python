# Updating dictionaries

# Adding a new key-value pair
student_info = {
    "name":"json",
    "cgpa":8.58
}
student_info["age"] = 21
print("New student info :",student_info)

# Updating value of a key
student_info["cgpa"] = 8.40

# Updating with another dictionary
new_student_info = {
    "name":"json123",
    "cgpa":8.41,
    "age":22
}
student_info.update(new_student_info)
print("New student info as follow :",student_info)

# Updating with key arguments
student_info.update(age=21,cgpa=8.40,city="chennai")
print("New student info :",student_info)

# using setdefault to add default values
new_student_info.setdefault("college","unknown") # default value of college for all students is "unknown"
print("New student info :",new_student_info)