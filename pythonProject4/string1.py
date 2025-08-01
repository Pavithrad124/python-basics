#program 1
s="Hello All22"
n=''
for i in s:
    if i.islower():
        n+=i.upper()
    else:
        n+=i.lower()
print(n)

#program 2
s=input().lower()
r=s[::-1]
if r==s:
    print("palindrome")
else:
    print("false")

#Anagram
n1="batman"
n2="manbat"
dic={}
for i in n1:
    dic[i]=dic.get(i,0)+1
for i in n2:
    dic[i]=dic.get(i,0)-1
flag=True
for i in dic.values():
    if(i!=0):
        print("not anagram")
        flag=False
        break
if(flag):
    print("anagram")

#or
n1="batman"
n2="mapbat"
s1=sorted(n1)
s2=sorted(n2)
print(s1)
print(s2)
if s1==s2:
    print("anagram")
else:
    print("not anagram")

#reversing word
s="hello"
x=s.split()
a=[]
for i in x:
    a.append(i[::-1])
res="".join(a)
print(res)

#swapping
a=2
b=5
c=a
a=b
b=c
print(a,b)

#swapping 2 char
s="abcdefghi"
res=""
for i in range(0,len(s),2):
    if(i==len(s)-1):
        res+=s[i]
        continue
    else:
        res+=s[i+1]
    res+=s[i]
print(res)

