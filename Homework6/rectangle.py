class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def square(self):
        """ Return a list containing a True for a vowel in the word,
               a False for a non-vowel.

           # >>> find_vowels('detestable')
           # >>> [False, True, False, True, False, False, True, False, False, True]
           """

#TODO як зробити док тест
        return self.length * self.width

    @staticmethod
    def generic_square(width, length):
        return width * length

