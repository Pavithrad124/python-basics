#to finf max no
li=[1,6,4,66,87]
n=li[0]
for i in li:
    if i>n:
        n=i
print(n)

#to find min no
li=[1,6,4,66,169,87]
n=li[0]
for i in li:
    if i<n:
        n=i
print(n)

#tuple
tu=(1,2,3)
tu1=list(tu)
tu1.append(4)
tu1=tuple(tu1)
print(tu1)

#remove duplicate values
li=[6,5,2,6,1,7,1]
list=[]
for i in li:
    if i not in list:
        list.append(i)
print(list)

#print duplicate values
li=[6,5,2,6,1,7,1]
list=[]
for i in range(len(li)-1):
    for j in range(i+1, len(li)):
        if(li[i] == li[j]):
            list.append(li[i])
print(list)

#using list
li=[3,4,1,6,7,8]
li2=[]
sum=0
for i in li:
    sum=sum+i
print(list)
