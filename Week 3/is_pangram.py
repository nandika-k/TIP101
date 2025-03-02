def is_pangram(my_str):
    if len(my_str) < 26:
        return False
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in alphabet:
        if letter not in my_str.lower():
            return False
    return True

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))