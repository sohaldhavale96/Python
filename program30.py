# Nested function
def min_max(nums:list):
    def find_min(nums):
        return min(nums)
    def find_max(nums):
        return max(nums)
    return find_min(nums), find_max(nums)

ls = [1,10,9,2,8,3,7,4,6,5]
print(min_max(ls))