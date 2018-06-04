"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE: 1
LOWER CASE: 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def calculate(sentence: str = input("Type some sentence:\n")):
    """
    lalalalal
    :param sentence:
    :return:
    """
    upper_case = 0
    lower_case = 0

    for letter in sentence:
        if letter.isupper():
            upper_case += 1
        elif letter.islower():
            lower_case += 1
    print(f'UPPER CASE: {upper_case}')
    print(f'LOWER CASE: {lower_case}')

if __name__ == '__main__':
    calculate()
