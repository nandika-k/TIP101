def create_dictionary(keys, values):
    dict = {}
    for i in range (len(keys)):
        dict[keys[i]] = values[i]
    return dict

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))