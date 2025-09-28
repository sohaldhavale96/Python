# Accessing items from dictionary

# Using square brackets
student_info = {
    "name":"Json",
    "email":"json@gmail.com",
    "age":21,
    "isMarried":False,
    "CGPA":8.40,
    "skills":["C","Java","Python"]
}
'''
print("Skills of students :",student_info["skills"])
print("CGPA of student :",student_info["CGPA"])
'''

# using get()
'''
print("Email of student :",student_info.get("email"))
print("age of student :",student_info.get("ega","Not Available")) # if not available, it will show "Not Available"
'''
# Iterating through keys
'''
keys_in_student_info = []
for key in student_info:
    print(f"{key} : {student_info.get(key)}")
    keys_in_student_info.append(key)
print("keys :",keys_in_student_info)
'''

# Iterating through key, value
for key, value in student_info.items():
    print(f"{key} : {value}")