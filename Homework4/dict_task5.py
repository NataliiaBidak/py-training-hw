"""
Write a Python program to get the depth of a dictionary
"""
import math

d1 = {}
d2 = {1: {}}
d3 = {1: {2: {}}}
d4 = {1: {2: {3: {6}}}}


def depth_of_dictionary(dictionary: dict):
    length = 0
    list_of_curly_braces = []
    for x in str(dictionary):
        if x == "}":
            length += 1
            list_of_curly_braces.append(length)
        elif x == "{":
            length -= 1
            list_of_curly_braces.append(length)

    return int(max(list(map(lambda x: math.fabs(x), list_of_curly_braces))))


print(depth_of_dictionary(d1))
print(depth_of_dictionary(d2))
print(depth_of_dictionary(d3))
print(depth_of_dictionary(d4))
print(d4[1][2][3])
