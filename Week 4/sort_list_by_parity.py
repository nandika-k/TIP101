def sort_array_by_parity(nums):
    even = []
    odd = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return (even + odd)

nums = [3,8,1,2,4,9]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

"""
def  sort_array_by_parity(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        if nums[left] % 2 > nums[right] % 2 :
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
        
        if nums[left]%2 == 0:
            left += 1

        if nums[right]%2 ==1:
            right -=1
    return nums
        
nums = [3,8,1,2,4,9]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
"""