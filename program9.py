# String methods
# String in python come with a variety of built-in methods that allow you to manipulate and work with them.

# upper() and lower()
text = "Hello World"
upper_text = text.upper() # Capitalise every letter
lower_text = text.lower() # convert every letter in lowercase
print(f"Original : {text}, Upper text : {upper_text}, Lower text : {lower_text}")

# capitalize() and title()
text = "Hello World"
capitalized_text = text.capitalize() # Capitalize first letter of string
titled_text = text.title() # Capitalize first letter of every word.
print(f"Original : {text}, Capitalize : {capitalized_text}, title : {titled_text}")

# strip() and lstrip() and rstrip()
text = "   Hello World  "
strip_text = text.strip() # remove whitespaces from both side
lstrip_text = text.lstrip() # remove leading whitespaces
rstrip_text = text.rstrip() # remove trailing whitespaces
print(f"""
    Original : {text},
    Stripped : {strip_text},
    left stripped : {lstrip_text},
    right stripped : {rstrip_text}
""")

# startswith() and endswith()
text = "filename.txt"
startswith_filename = text.startswith("filename")
endswith_extension = text.endswith(".txt")
print(f"""
    Original : {text},
    Starts with "filename" : {startswith_filename},
    Ends with ".txt" : {endswith_extension}
""")

# replace(old, new)
text = "This is user."
replaced_text = text.replace("user","Json")
print(f"""
    Original : {text},
    replaced text : {replaced_text}
""")

# find(substring)
text = "This is bigger string making no sense."
find_bigger = text.find("bigger") # if exists, return lowest index, otherwise returns -1
print(f"Is there : {find_bigger}")

# index(subtring)
text = "This is bigger string making no sense."
index_making = text.index("making") # if exists, return index, otherwise throws an error
print(f"Is there : {index_making}")
# if not sure that string exists or not, better to use try-catch.
try:
    index_making = text.index("make")
except:
    print(f"string not found.")

# split(seperator)
text = "This is bigger string making no sense."
split_text = text.split(" ")
print(f"""
    Original : {text} , 
    splitted : {split_text} ,
    type of splitted : {type(split_text)}
""")

# join(iterable)
ls = ["This","Is","Titled","String."]
joined_list = " ".join(ls)
print(f"""
    Original : {ls},
    joined : {joined_list},
    type of joined list : {type(joined_list)}
""")

# count(substring)
text = """
    Lion is the king of jungle.
    Mango is king of fruits.
    Eagle is king of birds.
    Whale is king of fish.
"""
count_king = text.count("king")
print(f"Count of king word in text : {count_king}")