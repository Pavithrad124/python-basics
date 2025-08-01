'''#cupcakes
n=int(input())
arr=list(map(int,input().split()))
res=0
for val in arr:
    if val>=5:
        res+=val
print(res)

#5 substrings where char same
s=input()
d={}
for char in s:
    #if char not in d:
    d[char]=d.get(char,0)+1
total=0
for k,v in d.items():
    total+=(v*(v+1))//2
print(total)

#ascii value
s=input()
threshold=int(input())
res=''
curr_ascii=0
for char in s:
    curr_ascii+=ord(char)
    if curr_ascii>threshold:
        break
    else:
        res+=char
print(res)

n=int(input())
arr=list(map(int,input().split()))
pos,zeros=[],[]
for num in arr:
    if num==0:
        zeros.append(num)
    else:
        pos.append(num)
res=pos+zeros
print(*res)'''

#dinner
n=int(input())
arr=list(map(int,input().split()))
if n<=1:
    print(0)
else:
    arr.sort()
    print(arr[-1]+arr[-2])

#puzzle
