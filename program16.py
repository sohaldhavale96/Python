# List built in methods
numbers = [1,2,3,4,5]

# append(element)
numbers.append(100)
print("list after adding element 100 :",numbers)

# extends(iterable)
ints = [6,7,8,9]
numbers.extend(ints)
print("List after extending :",numbers)

# insert element at specific position : insert(index, element)
numbers.insert(0,100)
print("List after adding 100 at first position :",numbers)

# pop(index) or pop()
last_element = numbers.pop()
print("List after popping last element :",numbers)
element_3rd = numbers.pop(2)
print("List after deleting element at 2nd index :",numbers)

# count(element)
count_100 = numbers.count(100)
print("Occurrance of 100 in list :",count_100)

# sort(key=None, reverse=False)
numbers.sort()
print("List after sorting :",numbers)
numbers.sort(reverse=True)
print("List after sorting list in reverse order :",numbers)

# reverse()
numbers.reverse()
print("List after reversing :",numbers)

# copy()
copy_of_list = numbers.copy()
print("Copy of list :",copy_of_list)