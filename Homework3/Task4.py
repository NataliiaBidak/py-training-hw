"""
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
# TODO use list.count() function
# sentence1 = input("Type some sentence:\n").split(" ")
sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.".split(" ")


def frequency1(sentence=sentence):
    list_unic = list(set(sentence))
    return {word: sentence.count(word) for word in sorted(list_unic)}


# print((frequency1()))

# TODO use dict.fromkeys
# dict.fromkeys(seq[, value]))
def frequency2(sentence=sentence):
    dictionary = dict.fromkeys(sorted(sentence), 1)
    for word in sentence:
        dictionary[word] = sentence.count(word)
    return dictionary


print((frequency2()))
print("llllllllllllllllllllllllllllllllllllll")
# TODO use collections import Counter

from collections import Counter, defaultdict

counts = Counter(sorted(sentence))
for i in sorted(list(set(sentence))):
    print(i + ":", counts[i])

# TODO use collections defaultdict
print("defauldict")


def frequency3(sentence=sentence):
    d = defaultdict(int)
    for k, v in sorted(list(zip(sentence, [sentence.count(word) for word in sentence]))):
        d[k] += 1

    return d.items()


# print((frequency3()))
# def frequency(sentence=input("Type some sentence:\n").split(" ")):
#     """
#
#     :param sentence:
#     :return:
#     """
#     print(sentence)
#     dict = {}
#     # for n in sorted(sentence):
#     for n in sentence:
#
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict


# print(frequency())
from functools import reduce

# if __name__ == '__main__':
# print(list(filter(lambda x: x > 5, range(10))))
# print(list(map(lambda x: x > 5, range(10))))
# TODO: investigate reduce

# print(list(enumerate(range(10))))

# print(list(zip(range(10), range(10, 0, -1))))
