# """Flattens a nested list.
#
#         >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
#         >>> [1, 2, 3, 4, 5, 6, 7]
#     """
#
#
# def flattens_list1(small_list: list, new_list: list):
#     if not isinstance(small_list, int):
#         for _list in small_list:
#             if isinstance(_list, list):
#                 # nested_list.pop(small_list)
#                 # return nested_list.extend(flattens_list(small_list))
#                 return flattens_list1(_list, new_list)
#             else:
#                 new_list.append(_list)
#     else:
#         new_list.append(small_list)
#
#
# def flattens_list(nested_list: list):
#     new_list = []
#     for small_list in nested_list:
#         flattens_list1(small_list, new_list)
#
#     return new_list
#
#
# print(flattens_list([[1, 2, [3, 4]], [5, 6], 7]))
# print(flattens_list([[1, 2, [3, 4, 8, 9, [0, -1]]], [5, 6], 7]))
# # filter(lambda small_list: isinstance(small_list,list) for small_list in nested_list)



def flatten_list(nested_list, flattened=None):
    """
    Flattens a nested list.

    >>> flatten_list([[1, 2, [3, 4]], [5, 6], 7])
    >>> [1, 2, 3, 4, 5, 6, 7]
    """
    if flattened is None:
        flattened = list()

    for item in nested_list:
        if isinstance(item, list):
            flatten_list(item, flattened=flattened)
        else:
            flattened.append(item)

    return flattened


if __name__ == '__main__':
    flatten_list([1, 2, [3, 4], [5, 6], 7])
