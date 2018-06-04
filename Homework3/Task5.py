"""
Write a function that takes a number and returns the sum of its digits.
Raise exception if argument of the wrong type was passed
"""


def sum(number):
    """

    :param number:
    :return:
    """

    sum = 0
    for digit in number:
        if not digit.isnumeric():
            raise Exception("Wrong format")

        sum += int(digit)

    return sum

    # return sum([int(digit) for digit in number])


if __name__ == '__main__':
    number = input("Type some numbers:\n")

    print(sum(number))
