from functools import reduce
l=["rat","elephant","moon","dog"]
def longList(a1, a2):
    if (len(a1)>len(a2)):
        # print(a1,a2)
        return a1
    else:
        return a2
op = reduce(longList, l)
print(op)
