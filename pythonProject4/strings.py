#program 1
s='can\tt'
print(s)

#program 2
s="hello world"
print(s.upper())

#program 3
s="hello world"
print(s.islower())

#count method
s="hello world"
print(s.count('o'))

#program 4
s="12233224"
print(s.count('2',1,5))

#find method
s="welcome"
print(s.find("Welcome"))

#program 5
s="hlo Welcome Welcome"
print(s.find("Welcome",4))

#join method
s=['1','2','3',"bro","python"]
x="*".join(s)
print(x)

#split method
s="apple banana grapes"
x=s.split('p')
print(x)

#replace method
s="apple banana grapes"
s=s.replace('a','m')
print(s)

#program 6
s="apple banana grapes"
q=s.replace('a','m')
print(s,q)

#program 7
s="apple banana grapes"
q=s.replace('a','m',1)
print(s,q)

#program 8
s="apple banana grapes"
q=s.replace(' ',' *')
print(q)

#program 9
s="apple banana grapes"
q=s.replace('a',' ',1)
print(q)

#program 10
s="    apple banana grapes   "
print(s.strip())