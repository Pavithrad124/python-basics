#program 1
num=0
def a():
    print("hello")
    global num
    if(num==1):
        return "hi"
    num+=1
    print(a())
print(a())

#program 2
def a(n):
    print(n)
    if(n==5):
        return 0
    return a(n+1)
a(1)

#program 3
num=1
def a(n):
    global num
    print(n)
    if(n==num):
        return 0
    num+=1
    return a(n)
a(1)

#other method
def a(n):
    if(n==1):
        return 1
    return a(n-1)
print(a(5))

#program 4
num=1
def a(n):
    global num
    print(num)
    if(n==num):
        return 0
    num+=1
    return a(n)
a(5)

#program 5
num=1
def a(n):
    global num
    print(num)
    if(n==1):
        return 1
    num*=n
    return a(n-1)
a(5)

#sum of no's
l=[2,3,4,5,6]
def sumLi(nums,index):
    if(index==len(nums)):
        return 0
    return nums[index]+sumLi(nums,index+1)
print(sumLi(l,0))

#pattern
for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#sum of digits
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(int(n / 10))
print(sumDigits(143))
print(sumDigits(12345))

