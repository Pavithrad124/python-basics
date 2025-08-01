# multiple inheritance
class A:
    def one(self):
        print("One")
class B(A):
    def two(self):
        print("Two")
class C(B):
    def one(self):
        print("Three")
obj=C()
obj.one()
obj.two()

#inheritance
class A:
    def one(self):
        print("grand")
class B:
    def two(self):
        print("father")
class C(A,B):
    def three(self):
        print("son")
obj=C()
obj.one()
obj.two()
obj.three()