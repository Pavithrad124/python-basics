def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[12,10,3,15,6,9]
print("original array:",arr)
insertion_sort(arr)
print("sorted array:",arr)
