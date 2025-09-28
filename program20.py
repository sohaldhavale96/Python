# Dictionaries
# A dictionary is a built-in data type that respresents a collection of key-value pair. It is highly flexible and efficient data stucture used for mapping key to values.

# Key features of dictionaries
    # Each element in a dictionary consists of a key and its corresponding value. The key is a unique identifier for the value.
    # Unlike lists, dictionaries are unordered collections, which mean the order of elements is not guaranteed.
    # Dictionaries can be modified after creation. You can add, remove, or update key-value pairs.
    # Dictionaries can grow and shrink in size as needed.
    # Each key in dictionary must be unique. If you try to add a key that already exists, the new value will overwrite the existing one.

# Empty dictionary
empty_dict = {}
print("Empty dictionary :",empty_dict)

# Dictionary with key-value pairs
student_info = {
    "name":"Json",
    "email":"json@gmail.com",
    "age":21,
    "isMarried":False,
    "CGPA":8.40,
    "skills":["C","Java","Python"]
}
print("Student info dictionary :",student_info)

# Using dict keyword
voter = dict(name="json",age=22)
print("Voter dictionary :",voter)

# Nested dictionary
academic_info = {
    "name":"json",
    "degree":"B.Tech.",
    "sems":{
        "sem1":9.58,
        "sem2":9.40,
        "sem3":8.82,
        "current":{
            "number_of_subjects":19,
            "SGPA":8.15
        }
    }
}
print("Academic information :",academic_info)

# Using list of tuples
product_info = [("name","json"),("marks",8.40),("is_passed",True)]
product = dict(product_info)
print("Product info :",product)