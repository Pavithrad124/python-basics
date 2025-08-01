ip=int(input())
def check(val):
    assert(val!=0),"wrong"
    print(5/val)
check(ip)

try:
    ip=int(input())
    def check(val):
        if(val==0):
            raise IndexError("wrong")
            print(5/val)
            check(ip)
except NameError:
    print("hello")
except IndexError:
    print("out")