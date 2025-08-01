#multiplication
n=int(input("enter a no:"))
mul=1
while(n>0):
    mul*=n%10
    n//=10
print(mul)

#length of a no
n=int(input("enter a no:"))
count=0
while (n!=0):
    n//=10
    count+=1
print("length of number",count)

#print a pattern
rows = int(input())
for x in range(1,rows+1):
    for y in range(x*2-1):
        print("*",end=" ")
    print()