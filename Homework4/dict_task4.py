"""
Write a Python program to check if all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False

"""


def check_emptiness(list_of_dict: list):
    # for x in lst:
    #     if len(x) == 0:
    #         return True
    #     else:
    #         return False
    return not any(list_of_dict)

print(check_emptiness([{}, {}, {}]))
print(check_emptiness([{1: 2}, {}, {}]))
