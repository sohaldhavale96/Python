# Lambda function
# Lambda function is a small anonymous function defined using a lambda keyword. It is often referred to as a "lambda expression". Lambda functions are used when you need a simple function for a short period and dont want to formally define a full function using the def keyword.

# example
add = lambda x,y:x+y

print("Addition of",add(1,2))


# Function that take another function as a argument
def addition_of_minmax(nums:list, minmax):
    return sum(minmax(nums))

ls = [1,2,3,4,5,6,7,8,9,10]
print("Addition of min and max element in list :",
      addition_of_minmax(ls,lambda ls:(min(ls),max(ls)))
    )