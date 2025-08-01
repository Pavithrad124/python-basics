def binary_search(l1,target):
    low=0
    high=len(l1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if l1[mid]<target:
            low=mid+1
        elif l1[mid] > target:
            high= mid - 1
        else:
            return mid
    return -1
l1=[1,2,3,4,5,6,7,8,9,10]
target=7
result=binary_search(l1,target)
if result!=-1:
    print("element is present at index",result)
else:
    print("element is not present")


