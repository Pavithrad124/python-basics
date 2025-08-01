#1 program
def user_name(name):
    return "hello"+name

a=lambda n1:n1+10
print(user_name("wini"))
print(a(5))

#2 program
def user_name(*nums):
    print(nums)

a=lambda *n1:print("hi",n1)
a("abc","mn","xyz")

#3 program
def user_name(*nums):
    print(nums)
a=lambda *n1:print(sum(n1))
a(4,9,5,6)

#4 program
def user_name(*nums):
    print(nums)
a=lambda *n1:print(list(reversed(n1)))
a(4,9,5,6)


a=lambda n1,n2=2:print(n1,n2)
a(n1=8,n2=4)

