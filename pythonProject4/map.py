l=[1,4,6]
def add1(n1):
    return n1+2
op=map(add1,l)
print(list(op))

#multi
l=[1,4,6]
def mul1(n1):
    return n1*n1
op=map(mul1,l)
print(list(op))

#sum of no
l=[[2,1],[3,5,6],[2,1,3]]
def add1(n1):
    return sum(n1)
op=map(add1,l)
print(list(op))

#multiply
l=[[2,1],[3,5,6],[2,1,3]]
def mul1(n1):
    res=1
    for i in n1:
        res*=i
    return res

op=map(mul1,l)
print(list(op))


no=[[3,2,3,1],[6,5,4],[9,8,7,0]]
def add1(n1):
    return sorted(n1)
op=map(add1,no)
print(list(op))
