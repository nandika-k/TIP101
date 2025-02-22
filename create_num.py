"""
PLAN
Declare string
for num in digits
    concat to string
convert string to int
return string
"""


def list_to_number(digits):
    num=""
    for digit in digits:
        num += str(digit)
    return int(num)

digits = [1,0,3]
number = list_to_number(digits)
print(number)