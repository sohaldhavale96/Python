# List unpacking
numbers = [12,3,4,5]
a,b,c,d = numbers

print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

numbers = [1,2,3,4,5,6,7,8,9,10]
first,second,*rest = numbers
print("First :",first)
print("Second :",second)
print("Rest elements :",rest)