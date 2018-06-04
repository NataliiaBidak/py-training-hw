'''
Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
'''

# from rectangle import Rectangle
#
# print(Rectangle.generic_square(3, 4))
#
# new_square = Rectangle(5, 6)
# print(new_square.square())
# import psutil
# for proc in psutil.process_iter():
#     # print(proc.name())
#     if 'firefox' in proc.name().lower():
#         proc.kill()

# assert not any(list(map(lambda x: 'firefox' in x, [x.name().lower() for x in psutil.process_iter()])))

# def sum_numbers(numbers: list = None):
#     if numbers == []:
#         return 0
#     if numbers == None:
#         return sum(range(101))
#     return sum(numbers)
#
#     print(sum_numbers())
#     print(sum_numbers([]))
#
#
# a = None
# print()

# NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
#          'julian sequeira', 'sandra bullock', 'keanu reeves',
#          'julbob pybites', 'bob belderbos', 'julian sequeira',
#          'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
#
#
# def dedup_and_title_case_names(names):
#     return [str(x.split()[0].capitalize()+' '+x.split()[1].capitalize()) for x in list(set(names))]
#
#
# def sort_by_surname_desc(names):
#     """Returns names list sorted desc by surname"""
#     names = dedup_and_title_case_names(names)
#     def takeSecond(elem):
#         return elem.split()[1]
#     return [str(x.split()[0].capitalize()+' '+x.split()[1].capitalize()) for x in sorted(names,reverse=True, key=takeSecond)]
#     # ...
#
#
# def shortest_first_name(names):
#     """Returns the shortest first name (str)"""
#     names = dedup_and_title_case_names(names)
#     min = names[0].split()[0]
#     for x in list(set(names)):
#         if len(x.split()[0])<len(min):
#             min = x.split()[0]
#
#     return min.capitalize()
#     # ...



#
# def rotate(string, n):
#     list_of_chars=list(string)
#     for x in list_of_chars[:n]:
#         a = x
#         list_of_chars.remove(x)
#         list_of_chars.append(a)
#     return ''.join(list_of_chars)
#
# a = rotate('hello',-2)
# print(a)



import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    with open('dictionary.txt') as dict_file:
        return list(map(lambda x: x.strip("\n"), dict_file.readlines()))


#
# def calc_word_value(word):
#     """given a word calculate its value using LETTER_SCORES"""
#     pass
#
#
# def max_word_value(words=None):
#     """given a list of words return the word with the maximum word value"""
#     pass

print(load_words())
