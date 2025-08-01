#list
l=[2,3,45,5,65,8]
def fil(n1):
    return n1<=8
op=filter(fil,l)
print(list(op))

#String
names=["abhishek","hasina","arjun","surya","jo","haarith"]
def name(n1):
    return (len(n1)<=5)
op=filter(name,names)
print(list(op))
