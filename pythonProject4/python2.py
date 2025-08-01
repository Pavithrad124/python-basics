#type of datatype
a=int(5.12)
b=float(6)
print(a,b)
print(type(a))

#assci
a=chr(97)
b=int('57')
print(a,b)
print(type(b))

#string
a='5'
b='2'
p=int(a)+int(b)
print(p)

#addition
a=132
b=54
p=int(a+b)
print(p)

#int to str
a=123
b=45
print(str(a)+str(b))

#operators
a=5
a+=a
b=4
b%=4
c=9
c/=c
d=2
d//=d
print(a)
print(b)
print(c)

#assign
x=1
y=7
print(x==y)
m=9
n=0
print(m!=n)
a=8
b='8'
print(a==int(b))

#right shift
a=4
print(a>>1)
#left shift
b=2
print(a<<2)

a='python'
b='is'
c='easy'
print(a,end="")
print(b)
print(c)

a='python'
b='is'
c='easy'
print(a,b,c,sep=' ',end=" ")

a=2
b=6
print(a,'*',b,'=',a*b)

print('22','02','2025',sep='-',end='\n')
print('red','blue','purple',sep=',',end='@')
print('black',end=" ")
print("green")

#format statements
print('hello {1} and {0}'.format("aa","bb"))
print('hello {1} and {1}'.format("aa","bb"))

name="wini"
age=25
print(f'hello {name} your age is {age}')
