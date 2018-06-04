# Replacing multiple characters in a string


def replace(text, old_chars, new_chars):
    """ Return text with old chars replaced with new chars.
    
    # >>> replace('heWlXo theYreZ', 'WXYZ', 'YZWX')
    # >>> 'heYlZo theWreX'
    """

    # your code here

    dict3 = {}

    for idx, i in enumerate(old_chars):
        dict3[i] = new_chars[idx]

    text1 = ""

    for x in text:
        if x in dict3.keys():
            text1 += dict3.get(x)
        else:
            text1 += x
    return text1


print(replace('heWlXo theYreZ', 'WXYZ', 'YZWX'))


import math
print(math.sqrt(25).is_integer())
