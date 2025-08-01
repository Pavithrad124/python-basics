#heirarchy
class A:
    def one(self):
        print("grand")
class B(A):
    def two(self):
        print("father")
class C(A):
    def three(self):
        print("son")
class D(A):
    def four(self):
        print("son1")


obj=C()
obj.one()
obj.three()

#hybrid inheritance
class A:
    def one(self):
        print("grand")
class B(A):
    def two(self):
        print("father")
class C(A):
    def three(self):
        print("son")
class D(B,C):
    def four(self):
        print("son1")
obj=C()
obj.one()
obj.three()

