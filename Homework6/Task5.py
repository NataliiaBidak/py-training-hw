class Widget():
    def __init__(self, name):
        self.name = name
        self.list_of_objects = []

    def add_dependency(self, *args):
        for object1 in args:
            self.list_of_objects.append(object1)

    def build(self):
        for object1 in self.list_of_objects:
            print(object1.name)


luke = Widget("Luke")
hansolo = Widget("Han Solo")
leia = Widget("Leia")
yoda = Widget("Yoda")
padme = Widget("Padme Amidala")
anakin = Widget("Anakin Skywalker")
obi = Widget("Obi-Wan")
darth = Widget("Darth Vader")
_all = Widget("All")

# luke.add_dependency(hansolo, leia, yoda)
# leia.add_dependency(padme, anakin)
# obi.add_dependency(yoda)
# darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
