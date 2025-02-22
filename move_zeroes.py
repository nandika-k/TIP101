"""
PLAN:
Declare output list
Declare var to count zeros

Iterate through nums
    If num is not a zero
        append to output
    else
        increase count of zeroes

Run for loop based on count of zeroes
    append 0 to output

return output
"""

def move_zeroes(nums):
    output=[]
    zeroes = 0

    for num in nums:
        if num != 0:
            output.append(num)
        else:
            zeroes += 1

    for i in range(zeroes):
        output.append(0)

    return output

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)