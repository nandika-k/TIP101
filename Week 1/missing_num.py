"""
PLAN
Sort nums
if num[0] != zero, return 0
Declare variable prev
Iterate through nums
    If item = 0, break
    Else, check if item is 1 more than prev
        If greater by more than 1, return that num
"""


def find_missing(nums):
    nums.sort()
    #print(nums)
    if nums[0] != 0:
        return 0
    
    prev = 0
    for num in nums:
        if num != 0 and num > (prev + 1):
            return (prev+1)
        prev = num

    """
    Other method
        nums = [2,4,1,0,5]
        missing_num = find_missing(nums)
        print(missing_num)
    """

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)