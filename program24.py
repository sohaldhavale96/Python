# Sets
# A set is an unordered collection of unique elements. Sets are defined by enclosing a comma-seperated sequence of values in curly braces{}. Unlike lists or tuples, set do not allow duplicate elements, and the order of elements is not guaranteed.

# declaring set
my_set = {1,2,3,4,5,2,1,3}
print("Set :",my_set)

# set from list
list_of_elements = [1,5,3,1,3,7,8,2,4,7,10]
my_set = set(list_of_elements)
print("Set :",my_set)

# Accessing elements using indices in set is not allowed, elements are arranged in unordered format.

# Adding element in set
my_set.add(99)
print("New set :",my_set)

# Adding multiple elements in a set using list
my_set.update([100,22,123,12])
print("New Set :",my_set)

# Adding multiple elements in a set using tuple
my_set.update((1001,221,1123,112))
print("New Set :",my_set)

# deletion in set
my_set.remove(3)
print("New set :",my_set)

# clear set
'''
my_set.clear()
print("New set :",my_set)
'''

# Iterating over set
for num in my_set:
    print("I am set element :",num)