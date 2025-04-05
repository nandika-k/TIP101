def first_occurence_of(haystack:str, needle:str):
    if needle not in haystack:
        return -1
    return haystack.find(needle)
    
print(first_occurence_of("sad", "sada"))