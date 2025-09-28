# Deleting in Dictionary

# del statement
student_info = {
    "name":"json",
    "cgpa":8.58
}
print("Original Dictionary :",student_info)
del student_info["cgpa"]
print("Dict after deletion :",student_info)

# pop method
student_info = {
    "name":"json",
    "cgpa":8.58
}
student_info.pop("name")
print("Dict after deletion :",student_info)

# popitem() method : remove last key
student_info = {
    "name":"json",
    "cgpa":8.58
}
student_info.popitem()
print("Dict after deletion :",student_info)


# clear() method : clear all keys
student_info = {
    "name":"json",
    "cgpa":8.58
}
student_info.clear()
print("Dict after deletion :",student_info)