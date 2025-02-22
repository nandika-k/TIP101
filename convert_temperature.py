"""
Edge Cases
 - temp = 0
 - integer input


PLAN:
Make an empty list
Do the conversion to Kelvin and Fahrenheit and store into list
Return list
"""


def convertTemp(celsius):
    temp = [f"{(celsius + 273.15):.2f}", f"{(celsius * 1.80 + 32.00):.2f}"]
    return temp

print(convertTemp(23.00))