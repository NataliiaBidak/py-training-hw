"""
Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

"""


def combine_two_dicts(dict1: dict, dict2: dict):
    for x in dict2:
        if x not in dict1:
            dict1.update({x:dict2.get(x)})
        else:
            dict1.update({x: dict2.get(x)+dict1.get(x)})
    return dict1


print(combine_two_dicts({'a': 100, 'b': 500, 'c': 800}, {'a': 300, 'b': 200, 'd': 400}))
