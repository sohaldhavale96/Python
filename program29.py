# Return statement
# A return statement is used within a function to send a value back to the caller. When a function is executed and encounters the return statement, it is immediately stops executing, and the specified value is sent back to the caller.

def min_max_sum_avg(nums:list)->tuple:
    try:
        minimum = min(nums)
        print(minimum)
        maximum = max(nums)
        summation = sum(nums)
        average = summation / len(nums)
        return minimum, maximum, summation, average
    except:
        print("err : List can't be empty.")

ls = [1,2,3,4,5,6]
# ls = []
print("Ans :",min_max_sum_avg(ls))