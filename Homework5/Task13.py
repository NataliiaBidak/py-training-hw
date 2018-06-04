"""
Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

"""


def sort_words(sequense: str):
    return "-".join(sorted(sequense.split("-")))

if __name__ == '__main__':
    print(sort_words("green-red-yellow-black-white"))
