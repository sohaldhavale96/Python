# List
# A list is a data structure that can store collection of items. It is one of the built-in data types and is commonly used to hold an ordered sequence of elements. Lists can contain elements of different data types, including numbers, strings, and even other lists.

'''
numbers = [1,2,3,4,5]
count = 0
for num in numbers:
    if num%2==0:
        count += 1
print("Count of even numbers :",count)
fruits = ["apple","mango","orange","watermelon"]
for fruit in fruits:
    print(f"{fruit}",end=" | ")
print()
mixed = [1, 3.14, "Hello", True]
for item in mixed:
    print(f"Type of {item} is {type(item)}.")
'''


# Accessing List items
# they are 0 based index
numbers = [1,2,3,4,5]
'''
print("First element : ",numbers[0])
print("Last element : ",numbers[len(numbers)-1])
print("Last element : ",numbers[-1])
'''

# traversing list in reverse order
'''

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])

'''

# Accessing elements using slices
# following codes may throw an error
'''
try:
    print(numbers[1:19])
    print(numbers[:5])
    print(numbers[3:])
    print(numbers[::-1])
except:
    print("An error occurred!")
'''


# Updating elements in a list
'''
numbers = [1,2,3,4,5]
print("List before :",numbers)
numbers[3] = 12
print("List after :",numbers)
'''

# Deleting element from a list
'''
numbers = [1,2,3,4,5]
print("List before :",numbers)
del numbers[3]
print("List after :",numbers)
# using remove(element)
numbers.remove(1)
print("After deleting element :",numbers)
'''