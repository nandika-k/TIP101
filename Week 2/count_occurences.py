def count_occurrences(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    return dict

nums = [1, 2, 2, 3, 3, 3, 4]
output = count_occurrences(nums)
print(output)