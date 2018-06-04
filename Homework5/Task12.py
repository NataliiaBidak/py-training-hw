"""
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

"""

import string


def pangram(sentence: str):
    """

    :param sentence:
    :return:
    """
    alphabet_list = string.ascii_lowercase
    return all(x in sentence for x in alphabet_list)

if __name__ == '__main__':
    print(pangram("The quick brown fox jumps over the lazy dog"))
    print(pangram("The quick brown foxxxxxxxxxx jumps over the lazy dog"))
