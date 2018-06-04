"""
Write a multiplication function (using addition (recursion))
 def my_mul(a, b) -> return a times b

"""


def my_multiplication(number, x):
    if x <= 1:
        return number
    else:
        return number + my_multiplication(number, x - 1)

if __name__ == '__main__':
    print(my_multiplication(10, 4))
