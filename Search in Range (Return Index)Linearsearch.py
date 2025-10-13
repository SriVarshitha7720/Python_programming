def Range(arr,target,start,end):
    if not arr:
        return False
    for index in range(start,end+1):
        if arr[index]==target:
            return index
        return False
arr=[1,2,3,4,5,6,7,78]
start=1
end=5
target=2
print(Range(arr,target,start,end))