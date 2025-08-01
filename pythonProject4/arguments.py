#Method 1
li=[1,2,3,1,5,1,4, [4, 6, 1, 1]]
n=0
for i in li:
    if(i==1):
        n+=1

print(n)

#Method 2
li=[1,2,3,1,5,1,4, [4, 6, 1, 1]]
n=0
for i in li:
    if(type(i)==list):
        for j in i:
            if(j==1):
                n+=1
    elif():
        n+=1
print(n)
