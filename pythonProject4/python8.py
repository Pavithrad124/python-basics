n=int(input())
input=str(n)
li=[]
for i in input:
    if i not in li:
        li.append(i)
print(li)
dic={}
while (n>0):
    count=n%10
    dic[count]=dic.get(count,0)+1
    n//=10
print(dic)
for i in li:
    print(f"{i} - {dic.get(int(i))}")

