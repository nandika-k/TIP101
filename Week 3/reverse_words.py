"""
Remove extra space
Reverse the words


"""

def reverse_words(sentence):
    #output = sentence.strip()
    # .split() gets rid of trailing and leading spaces
    words = sentence.split()

    output = ' '.join(words[::-1])
    #output = reverse() is another option
    #reverse(words) is also an option
    return output

input = "  the sky   is  blue     "
print(reverse_words(input))