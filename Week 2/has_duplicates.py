def hasDuplicates(nums, k):
    dict = {}
    nums2 = nums[0:k]

    for i in nums2:
        if i in dict:
            return True
        else: 
            dict[i] = 1
    return False

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)