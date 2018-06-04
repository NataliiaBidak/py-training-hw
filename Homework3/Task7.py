"""
Write a function that takes a list of strings AND a minimum length (number) and returns only the strings that are longer than
the provided number.
Example Usage:
# returns the list: ['baby', 'more', 'time']
longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')
"""


def longer_than( *args,length: int):
    """

    :param args:
    :param length:
    :return:
    """
    list_ = []
    for word in args:
        if len(word) > length:
            list_.append(word)

    return list_


print(longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time'))
