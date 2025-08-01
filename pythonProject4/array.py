#1 program
import numpy
arr=numpy.array([[[10,6],[7,8]],[[1,2],[3,4]]])
print(arr[1,1,1])

#2 program
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in arr1:
    for y in x:
        print(y)

#3 program
import numpy as np
arr1=np.array([1,2,3,4,5])
for i in range(0,len(arr1)):
    if(arr1[i]==3):
        arr1[i]=8
print(arr1)

#4 program
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
for i in range(0,len(arr1)):
    for j in range(0,len(arr1[0])):
        if(arr1[i,j]==5):
            arr1[i,j]=100
        print(arr1[i,j],end=" ")
    print()

#5 program
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(0,len(arr1)):
    for j in range(len(arr1[0])-1,-1,-1):

        print(arr1[i,j],end=" ")
    print()

#6 prograqm
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(len(arr1)-1,-1,-1):
    for j in range(0,len(arr1[0])):
        print(arr1[i,j],end=" ")
    print()

#7 program
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(len(arr1)-1,-1,-1):
    for j in range(len(arr1[0])-1,-1,-1):
        print(arr1[i,j],end=" ")

    print()

#8 program
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(len(arr1)):
    sum=0
    for j in range(len(arr1[0])):
        sum+=arr1[i][j]
    print(sum)

#9 program
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in range(len(arr1)):
    sum=0
    for j in range(len(arr1[0])):
        sum+=arr1[j][i]
    print(sum)