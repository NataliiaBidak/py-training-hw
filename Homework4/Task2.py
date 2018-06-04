"""
16 пункт є  питання!!!
Write a function groupby that takes a key-function and a list.
The function should call key-function on all items in the
list and return a dictionary whose keys are the results of key-function and
values are all values from the list that product that key.

Example Usage:

groupby(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here')

# returns: { h: ['hello', 'hi', 'help', 'here'], b: ['bye'] }

"""


def groupby(func, list_of_el: list):
    result = {}
    for x in list_of_el:
        if result.get(func(x)):
            result.get(func(x)).append(x)
        else:
            result.update({func(x): [x]})

    return result


print(groupby(lambda s: s[0], ['hello', 'hi', 'help', 'bye', 'here']))
