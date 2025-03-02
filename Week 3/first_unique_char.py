def first_unique_char(my_str):
    chars = {}

    for i in range(len(my_str)):
        character = my_str[i]
        if character not in my_str[:i]:
            chars[character] = i
        elif character in chars:
            chars.pop(character)

    
    if len(chars) == 0:
        return -1
    elif len(chars) == 1:
        return chars.values()[0]
    else:
        lowest = len(my_str)
        for character, index in chars.items():
            if index < lowest:
                lowest = index
        return lowest


my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))