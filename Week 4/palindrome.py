def is_palindrome(word):
    rev_word = word[::-1]
    return word == rev_word

def first_palindrome(words):
    for word in words:
        if is_palindrome(word):
            return word
    return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)