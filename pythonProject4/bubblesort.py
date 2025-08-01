def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j + 1]=temp
arr=[30,14,13,19,20,5,10]
print("unsorted is:")
print(arr)
bubble_sort(arr)
print("sorted is:")
print(arr)



