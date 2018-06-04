"""
Write a custom power function (using recursion)
 	def my_pow(number, x) -> return number ^ x
"""


def my_power(number, x):
    if x <= 1:
        return number
    else:
        return number * my_power(number, x - 1)


if __name__ == '__main__':
    print(my_power(2, 4))

