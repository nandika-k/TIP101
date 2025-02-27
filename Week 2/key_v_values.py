def keys_v_values(dictionary):
    key_sum = sum(dictionary.keys())
    value_sum = sum(dictionary.values())

    if key_sum > value_sum:
        return "keys"
    elif value_sum > key_sum:
        return "values"
    else:
        return "balanced"


dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)