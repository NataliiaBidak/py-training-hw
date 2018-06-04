class Circle:
    def __init__(self, r):
        self.radius = r

    def square(self):
        return 3.14 * self.radius ** 2

    @staticmethod
    def generic_square(radius):
        return radius * 3.14 ** 2

    def perimetr(self):
        return self.radius * 2 * 3.14

    @staticmethod
    def generic_perimetr(radius):
        return radius * 2 * 3.14
