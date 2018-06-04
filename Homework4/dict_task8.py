"""
Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]

"""
def highest_sum(lst: list):
    summ = 0
    for index,list1 in enumerate(lst):
        if sum(list1) > summ:
            summ = sum(list1)
            max_index = index

    return lst[max_index]

print(highest_sum([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))


def a(x: int):
    """
    some descr

    :param x:
    :return:
    """

    pass

