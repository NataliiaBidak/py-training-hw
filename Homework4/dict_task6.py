"""
Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]

"""


def remove_duplicates(lst: list):
    for list1 in lst:
        if lst.count(list1) != 1:
            lst.remove(list1)
    return lst


print(remove_duplicates([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
