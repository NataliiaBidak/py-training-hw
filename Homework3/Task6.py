"""
Write a function that returns the multiplication of all input arguments.
The function should ignore non-numeric arguments.
Example Usage:

# returns 200:
mymul('foo', 'bar', 10, 20)

# returns 1:
mymul()

# returns 7:
mymul(7)
"""


def mymul(*args):
    """

    :param args:
    :return:
    """
    sum = 1

    if not args:
        # sum = 1

        return sum

    for x in args:
        if type(x) == int:
            sum *= x

    return sum


print(mymul('foo', 'bar', 10, 20))
print(mymul())
print(mymul(7))
