#pattern 1
rows = int(input())
for x in range(1,rows+1):
    for y in range(x*2-1):
        print("*",end=" ")
    print()


#reverse
for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#pattern 2
rows=int(input())
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#pattern 3
for i in range(5):
    if (i==3):
        continue
    print(i)

#pattern 4
def pattern(n):
    for i in range(n):
        print(i,end=" ")
    print()
    pattern(4)

#pattern 5
def pattern(n1,n2):
    print(n1,n2)
    return "hello"
res=pattern(2,3)
print(res)

#pattern 6
for x in range(4):
    for y in range(4):
        print("*",end="")
    print()
