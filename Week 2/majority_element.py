def find_majority_element(elements):
    n = len(elements)/2
    majority_element = None
    dict = {}
    for i in elements:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for key, values in dict.items():
        if values > n:
            majority_element = key
    return majority_element

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))