def remove_duplicates(nums):
    pos = 1

    while pos != (len(nums) - 1):
        prev = nums[pos-1]
        curr = nums[pos]

        if curr == prev:
            nums.pop(pos)
        else:
            pos += 1
    return len(nums)

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list