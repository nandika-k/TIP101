from more_itertools import locate

def min_distance(words, word1, word2):
    word1_indices = list(locate(words, lambda x: x == word1))
    word2_indices = list(locate(words, lambda x: x == word2))
    min = len(words)
    for i in word1_indices:
        for j in word2_indices:
            dist = abs(i-j)
            
            if dist < min:
                min = dist

    return min

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)