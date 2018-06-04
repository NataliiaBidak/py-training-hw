"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

"""


def dict_from_string(string: str):
    d = {}
    d = d.fromkeys(sorted(string), 1)
    for letter in string:
        # d.update({letter: string.count(letter)})
        d[letter] = string.count(letter)
    return d


print(dict_from_string('w3resource'))
