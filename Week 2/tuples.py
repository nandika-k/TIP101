'''
You're given a list of tuples, where each tuple contains a category and
a value. Write a function to count how many items belong to each
category.
'''
'''
UNDERSTAND
Count # of items in each category

PLAN
Create a dictionary
Go through the list of tuples
    For each tuple, get the category - call it "category"
    Add 1 to the count of category in dictionary or create if it doesnt exist
Return the dictionary
'''


def count_by_category(items):
    cat_count = {}
    for pair in items:
        category = pair[0]
        if cat_count.get(category, None) != None:
            cat_count[category] += 1
        else:
            cat_count[category] = 1
    return cat_count

# input
items = [("fruits", "apple"), ("vegetables", "carrot"),
         ("fruits", "banana")]
print(count_by_category(items))
# expected output: {"fruits": 2, "vegetables": 1}