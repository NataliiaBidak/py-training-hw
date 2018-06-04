# Swapping list elements

import random

r = random.random


def swap_elements(in_list: list):
    """ Return the list after swapping the biggest integer in the list 
    with the one at the last position.
    
    >>> swap_elements([3, 4, 2, 2, 43, 7])
    >>> [3, 4, 2, 2, 7, 43]
    """

    # your code here
    max_index = in_list.index(max(in_list))
    in_list[max_index], in_list[-1] = in_list[-1], in_list[max_index]
    return in_list






# 5! = 1 * 2 * 3 * 4 * 5

def factorial(n):
    print(n)
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)





json_data = {
    'k1': True,
    'k2': [1,2,3,4],
    'K3': "123"
}