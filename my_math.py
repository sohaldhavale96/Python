def add(a, b):
    return a+b

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def subtract(a, b):
    return a-b

def div(a, b):
    try:
        return a/b
    except:
        print("Can't divide by 0")

def multiply(a, b):
    return a*b

def reminder(a, b):
    try:
        return a%b
    except:
        print('Error')