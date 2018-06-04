"""
Write a Python program to find all the values in a list are greater than a specified number
"""
def greater_than(lst:list, number:int):
    return [x for x in lst if x > number]
print(greater_than([34,56,23,1,45,2,3,87],25))