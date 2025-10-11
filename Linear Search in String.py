def Range(s,target):
    if len(s)==0:
        return False
    for c in s:
        if c==target:
            return True
    return False
s='Varshi'
target='s'
print(Range(s,target))