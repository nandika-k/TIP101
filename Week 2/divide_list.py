def divideList(nums):

    dict = {}

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for value in dict.values():
        if value % 2 != 0:
            return False
    return True

nums = [3, 2, 3, 2, 2, 2]
print(divideList(nums))