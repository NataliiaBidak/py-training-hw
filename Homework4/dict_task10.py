"""
Write a Python program to sort a list alphabetically in a dictionary.
 	input: {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
output: {'n1': [1, 2, 3], 'n3': [2, 3, 4], 'n2': [1, 2, 5]}

"""

def sort_list(d:dict):
    for key,value in d.items():
        value.sort()
        d[key] = value
    return d
print(sort_list({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}))