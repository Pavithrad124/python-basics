#factorial of a no(Method 1)
n=int(input("enter a number:"))
def factorial(n):
    result=1
    while(n>1):
        result*=n
        n-=1
    return result
print(f'factorial of {n} is {factorial (n)}')

#factorial of a no(Method 2)
n=int(input("enter a number:"))
count=1
fact=1
while(count<=n):
    fact*=count
    count+=1
print(fact)

#(Method 3)
n=int(input("enter a number:"))
count=1
fact=1
while(count<=n):
    fact*=count
    count+=1
print(fact)

