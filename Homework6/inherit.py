class A:
    attr_a = 123

    def __init__(self, a):
        self.a = a

    def m1(self):
        print(f"class A m1 called")

class AA:
    def m1(self):
        print(f"class AA m1 called")

class B(A):
    def __init__(self, a, b):
        self.b = b
        super().__init__(a)


class C(AA, A):
    def m3(self):
        print("m3 called")

a = A(42)
b = B(42, 33)
c = C(1)

# todo: get parent's name (A, AA in C)
