# Tuples
# Tuple is an ordered, immutable collection of elements. This means that once you create a tuple, you cannnot modify its contents. You can't perform create, update, delete operation on it. 

admins_list = ("admin","json")
print("Admins :",admins_list)

# we can't add, remove, update, delete from tuple
try:
    admins_list.add("new_user") # not allowed
    admins_list.remove("admin")
except:
    print("WARNING : Can't perform this operation. You can only read tuple.")

# weird thing about tuple
tuples = 1, 2, 3, 4, 5, 6, 2, 2
print(type(tuples))
count = tuples.count(2)
print("Count :",count)