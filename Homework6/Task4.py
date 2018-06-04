"""
Implement a class named Color.
It should construct color from hex value (e.g. #ffffff) and have optional name: ‘color’.
Add possibility to set and get name (property).
Add property rgb that returns rgb tuple of color
Add method to convert hex value to rgb tuple.
Add possibility to construct object from rgb value (classmethod).
Add methods to convert: hex > rgb; rgb > hex (staticmethod).
Add str and repr methods; add possibility to compare 2 colors (__eq__)

"""


class Color:

    def __init__(self, value, name='color'):

        self.value = value
        self._name = name

    def __str__(self):
        return f"This is an Obj of class {self.__class__.__name__}"

    def __repr__(self):
        return f"Obj of class {self.__class__.__name__}"

    def __eq__(self, other):
            return self.value == other.value

    def get_name(self):
        return self._name

    def set_name(self, color):
        self._name = color

    name = property(get_name, set_name)

    @property
    def rgb(self):
        return self.hex_to_rgb(self.value)

    @classmethod
    def from_rgb(cls, *rgb):
        return cls(Color.rgb_to_hex(rgb))

    @staticmethod
    def hex_to_rgb(value):
        h = value.lstrip('#')
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb: tuple):
        hex_line = "#"
        for element in rgb:
            hex_line += str(hex(element))[2:]
        return hex_line


color1 = Color('#ff01ff', name='black')
color2 = Color('#ff01ab', name='red')
color3 = Color('#ff01ab', name='blue')
color4 = Color('#aa01ab')
color5 = Color.from_rgb(111, 222, 123)

print(color3==color2.value)
print(color3.rgb_to_hex((156, 1, 1)))
print(color2.name)
color2.name = 'white'
print(color2.name)
print(color2.rgb)
print(color5.value)


#TODO https://www.webucator.com/blog/2015/03/python-color-constants-module/
