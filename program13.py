# Loops

# for loop
'''
ls = [1,2,3,4,5]
for i in ls:
    print(f"List item : {i}")
text = "#HelloWorld"
for char in text:
    print(f"Char : {char}")
text = "#HelloWorld"
for char in text:
    print(char.split(" "))
'''

# range
'''
for i in range(10): # starts from 0 and 10 is exclusive
    print(i,end=" ")
print()
for i in range(1,11): #print 1 to 10
    print(i,end=" ")
print()
for i in range(10,0,-1):
    print(i, end=" ")
print()
for i in range(10,0,-2):
    print(i, end="|")
'''

# while
'''
print("\nTable : ")
i = 0
num = 3
while(i<10):
    print(f"{3 * (i+1)}")
    i += 1
'''
