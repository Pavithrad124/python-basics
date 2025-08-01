#1 program
import numpy
arr=numpy.array([0,1,4,7,8])
print(arr[1])

#2 program
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(len(arr),len(arr1),len(arr1[0]))

#3rd program
import numpy as np
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
for x in range(len(arr1)):
    for y in range(len(arr1[0])):
        print(f"index {x} - {y} : {arr1[x][y]}")

#reversing string
a = str(input("Enter the string to be reversed: "))
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
print(reverse(a))

#using list
li=[2,3,4,55,70,100]
target=100
isPresent=False
for i in li:
    if target==i:
        print("target present")
        isPresent=True
        break
if(not isPresent):
    print("target not present")