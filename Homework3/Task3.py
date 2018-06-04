"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""


def net_amount():
    """

    :return:
    """
    b = []
    while True:
        a = input(
            'Enter the deposit or withdrawal in the next format : D 300 or W 200. When you done , press enter  :\n')
        if a == '':
            break
        b.append(a)
    deposits = [int(x[2:]) for x in b if "D" in x]
    withdrawal = [int(x[2:]) for x in b if "W" in x]

    return sum(deposits)-sum(withdrawal)


print(net_amount())
#TODO refactor