"""
Write a Python program to get the current time in Python.
Sample Format :  13:19:49.078205

"""
from datetime import datetime
print(datetime.now().time())




class Cirle:
    def __init__(self, r):
        self.radius = r


    def square(self):
        return 3.14 * self.radius ** 2

    @staticmethod
    def generic_square(radius):
        return radius * 3.1 ** 2




class A:

    class_c = 42

    def __init__(self, a, b, c=None):
        self._a = a
        self._b = b
        self._c = c

    def m(self, text):
        print(text)

    # @classmethod
    def c_method(cls):
        return "Classmethod called"

    c_method = classmethod(c_method)

    @staticmethod
    def s_method():
        return "Static"

    def get_a(self):
        return self._a

    def set_a(self, value):
        self._a = value

    a = property(get_a, set_a)

    def __str__(self):
        return f"This is an Obj of class {self.__class__.__name__}"


    def __repr__(self):
        return f"Obj of class {self.__class__.__name__}"

    def __int__(self):
        return self._a

    def __add__(self, other):
        return self.c + other