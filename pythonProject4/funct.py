#function 1
def add(x,y):
    print("hello")
    sum=x+y
    return sum
res=add(1,2)
print(res)

#function 2
def display(name,age):
    print("hello",name,age)
display("xyz",20)

#function 3
def add(*a):
    print(a)
    return a
res=add(2,3,4,5,6)
print(res)

#example 1
a="hi"
def add():
    global a
    a+="all"
    print("in",a)
add()
print("out",a)

#example 2
a="hi"
def add():
    print("in",a)
add()
a+="all"
print("out",a)

#using list
li=[1,2,"python",4,5]
for i in range(len(li)):
    print(li[i])

#addition of int & float
li=[1,2,"python",4,5.9,True]
sum=0
for i in li:
    if (type(i)==int or type(i)==float):
        sum=sum+i
print(sum)

