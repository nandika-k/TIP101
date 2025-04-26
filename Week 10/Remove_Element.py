#Problem 2: Remove Element
# Given a list of integers nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, for your response to be acceptable, you need to do the following things:
# Change the list nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k
def remove_element(nums, val):
    if nums.count(val) == len(nums) - 1:
        return 0
    replacementPointer = len(nums)-1
    for num in range(len(nums)):
        print(nums)
        if num == replacementPointer:
            break
        if nums[num] == val:
            while(nums[replacementPointer] == val):
                replacementPointer -=1
            nums[num], nums[replacementPointer] = nums[replacementPointer], nums[num]
    print(len(nums), replacementPointer)
    return len(nums) - replacementPointer
nums = [3,2,2,3]
print(remove_element(nums, 3))