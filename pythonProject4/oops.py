#example 1
class cloths:
    a=10
    def display(self,name):
        print("hello",name)
obj=cloths()
obj.display("abhi")
print(obj.a)

#example 2
class cloths:
    def __init__(self):
        print("hello")
    def __del__(self):
        print("deleted")
    def __str__(self):
        print("one")
        return "i am a string"

obj=cloths()
print(obj)
del obj