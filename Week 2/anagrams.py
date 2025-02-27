"""
Given a list of string, group the strings that are anagrams of each
other.
An anagram is defined as a word formed by rearranging the letters of 
another, such as "eat" and "tea"
"""

"""
PLAN
    Sort the word
    Store in dictionary by the sorted version
    Store a value of an array with all the matching words
Go through the dictionary and get each list
"""

def group_anagrams(words):
    wordlists = {}
    for word in words:
        key = sorted(word)
        print(key)
        lst = wordlists.get(key, [])
        lst.append(word)
        wordlists[key] = lst

words = ["eat", "tea", "tan", "ate", "nat", "bat"]