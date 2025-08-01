dic={1:"hello",2:"hi"}
print(dic.get(2))
print(dic.items())
for i,j in dic.items():
    print(i,j)

#dict
dict={1:1,2:1,3:0}
for x,y in dic.items():
    print(f'key is {x} - key is {y}')

dic={1:5,2:2,3:0}
for i in dic:
    dic[i]+=1
print(dic)

dic={ }
for i in range(10):
    dic[i]=dic.get(i,0)+1
    dic[i] += i
print(dic)

