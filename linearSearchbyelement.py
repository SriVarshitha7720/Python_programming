def linearSearch(arr,target):
    if not arr:
        return False
    for element in arr:
        if element==target:
            return element
    return False
arr=[1,2,3,4,5,6,56]
target=56
print(linearSearch(arr,target))