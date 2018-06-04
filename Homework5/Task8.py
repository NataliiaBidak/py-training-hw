"""
Write a Python program to determine whether a given year is a leap year.

"""

import calendar

print(calendar.isleap(1900))
print(calendar.isleap(1996))
print(calendar.isleap(2016))


def is_leap(x):
    if x % 4 == 0 and type(x % 400) == int and x % 100 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_leap(123))
    print(is_leap(1232))