'''common prefix
s=input().split()
s.sort()
i=0
first_word=s[0]
last_word=s[-1]
while i<len(first_word) and i<len(last_word) and first_word[i]==last_word[i]:
    i+=1
res=first_word[:i]
if len(res)==0:
    print("")
else:
    print(res)

#anagram
s,t=input().split()
s=list(s)
t=list(t)
s.sort()
t.sort()
if s==t:
    print("True")
else:
    print("False")

# h to l occuring letters
s=input()
d={}
for char in s:
    if char not in d:
        d[char]=1
    else:
        d[char]+=1
sorted_vals=sorted(d.items(),key=lambda x:[-x[1],x[0]])
arr=[]
for k,v in sorted_vals:
    arr.append(k)
print(arr)

#shift
s,goal=input().split()
if len(s)==len(goal) and goal in s+s:
    print("True")
else:
    print("False")

#Isomorphic
def isomorphic(s,t):
    if len(s)!=len(t):
        return "True"
    else:
        mapping={}
        used_chars=set()
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in used_chars:
                    return "False"
                mapping[s[i]]=t[i]
                used_chars.add(t[i])
            else:
                if mapping[s[i]]!=t[i]:
                    return "False"
        return "True"
s,t=input().split()
print(isomorphic(s,t))

#largest odd
s=input()
while len(s)>0:
    last_char=int(s[-1])
    if last_char%2!=0:
        print(int(s))
        break
    s=s[:len(s)-1]

nums=list(map(int,input().split()))
max_val=nums[0]
second_max=-1
for num in nums:
    if num>max_val:
        second_max=max_val
        max_val=num
    elif num>second_max and num!=max_val:
        second_max=num
print(second_max)

nums=list(map(int,input().split()))
count=1
max_count=-1
if 1 not in nums:
    print(0)
else:
    for i in range(1,len(nums)):

#string balance
def valid_parentheses(s):
    d={'}':'{',']':'[',')':'('}
    stack=[]
    for char in s:
        if char in '{[(':
            stack.append(char)
        elif stack and d[char]==stack[-1]:
            stack.pop()
        else:
            return False
    return len(stack)==0
s=input()
print(valid_parentheses(s))

#greater element
arr=list(map(int,input().split()))
res=[]
n=len(arr)
for i in range(n):
    next_greater=-1
    for j in range(i + 1, n):
        if arr[j]>arr[i]:
            next_greater=arr[j]
            break
    res.append(next_greater)
print(res)

#sum of min value
arr=list(map(int,input().split()))
res=0
n=len(arr)
mod=10**9+7
prev_min=[0]*n
next_min=[0]*n
stack=[]
for i in range(n):
    count=1
    while stack and stack[-1][0]>arr[i]:
        count+=stack.pop()[1]
    prev_min[i]=count
    stack.append((arr[i],count))

stack=[]
for i in range(n-1,-1,-1):
    count=1
    while stack and stack[-1][0]>arr[i]:
        count+=stack.pop()[1]
    prev_min[i]=count
    stack.append((arr[i],count))

print(prev_min,next_min)
res=0
for i in range(n):

#singly list
class LinkedList:
    def __init__(self,vol,next=Node):
        self.val=val
        self.next=next
def list_to_linkedlist(arr):
    node=LinkedList(0)
    curr=node
    for var in arr:
        curr.next=LinkedList(var)
        curr=curr.next
    return node.next
def reverseK(head,k):
    def reverse(start,end):
        prev,curr=None,start
        while curr!=end:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    count=0
    node=head
    while node:
        count+=1
        node=node.next
    dummy=Linkedlist(0)
    dummy.next=head
    prev,curr=dummy,head
    while count>=k:
        tail=curr
        for _ in range(k):
            tail=tail.next
        new_head=reverse(curr,tail)
        prev.next=new_head
        prev=curr
        curr.next=tail
        curr=tail
        count-=k
    return dummy.next
def print_linked_list(head):
    res=[]
    while head:
        res.append(head.val)
        head=head.next
    return "".join(map(str,res))
arr=list(map(int,input().split()))
k=int(input())
new_head=reverseK(arr,k)
print(print_linked_list(new_head))

#basketball contest
def max_score(N,K,A):
    max_score=0
    for i in range(N,K+1):
        curr=0
        for j in range(K):
            curr+=(j+1)*A[i+j]
        max_score=max(max_score,curr)
    return max_score
N=int(input())
K=int(input())
A=list(map(int,input().split()))
print(max_score(N,K,A))

#size of array
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
a,b=arr[-1],arr[-2]
avg=(a+b)/2
for i in range(len(arr)):
    if arr[i]<avg:
        arr[i]=0
print(sum(arr))

#smallest prime number
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
while True:
    n+=1
    if isprime(n):
        prime(n)
        break

#or
def isprime(n):
    if n<=1:
        return False
    factors=0
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(isprime(2**31-1))

#colors of houses
s=list(input())
n=len(s)
for i in range(len(s)):
    if s[i]=='W':
        if i==0:
            j=1
            while j<n:
                if s[j]!='W':
                    s[i]=s[j]
                    break
                j+=1
        else:
            s[i]=s[i-1]
badness=0
for i in range(1,n):
    if s[i]!=s[i-1]:
        badness+=1
print(badness)

#ant
def ant(N,A):
    position=0
    count=0
    for move in A:
        position+=move
        if position==0:
            count+=1
    return count
N=int(input())
A=list(map(int,input().split()))
print(ant(N,A))'''

#chocolate jar
def choc(n,arr):
    A=0
    for chocolates in arr:
        rounds=chocolates//3
        leftover=chocolates%3
        A+=rounds
        if leftover>=1:
            A+=1
    return A
n=int(input())
arr=list(map(int,input().split()))
print(choc(n,arr))