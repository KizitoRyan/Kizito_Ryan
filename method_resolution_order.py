class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):  # Class demonstrating multiple inheritance
    pass

d = D()
d.show()

#Method 1 to show MRO
print(D.mro())

#Method 2 to show MRO
help(D)
