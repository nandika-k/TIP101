"""
PLAN:
Declare output list
Iterate through list
    If odd (mod 2)
        add to list
return output
"""

def get_odds(nums):
    output = []
    for num in nums:
        if num % 2 == 1:
            output.append(num)
    return output

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)