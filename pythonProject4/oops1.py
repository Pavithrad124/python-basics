class calc:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b
    def truediv(self,a,b):
        if(a!=0 and b!=0):
            return a//b
        else:
            return "invalid"

calcu=calc()
print("add:",calcu.add(2,4))
print("sub:",calcu.sub(2,4))
print("mul:",calcu.mul(2,4))
print("div:",calcu.truediv(2,4))

