"""
PLAN
Declare sum var
Use a for loop to iterate through list
    Add num to sum variable
Divide sum by length of list

Use sum and len functions to calculate avg
"""

def average(scores):
    #sum=0
    # for num in scores:
    #     sum += num

    return sum(scores)/len(scores)

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)