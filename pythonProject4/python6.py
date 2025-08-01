#using list1
li=[3,4,1,6,7,8]
for i in range(len(li)-1):
    print(sum(li[i:i+2]))

#list2
li=[3,4,1,6,7,8]
k=3
for i in range(len(li)-k-1):
    print(sum(li[i:i+k]))