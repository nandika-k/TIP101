def print_pair (dictionary, target):
    # if target in dictionary:
    #     print("Key: ", target)
    #     print("Value: ", dictionary[target])
    # else:
    #     print("The pair does not exist!")
    value = dictionary.get(target, None)
    if value == None:
        print("This pair does not exist!")
    else:
        print("Key: ", target, "\nValue: ", value)

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")