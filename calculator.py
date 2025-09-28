def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if y==0:
        return "Can't divisible by zero"
    else:
        return a/b
print("Select option :")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")
while True:
    ch=int(input("Enter 1/2/3/4 and 'q' for quit"))
    if ch=='q':
        print("Quiting")
        break
    if ch in ('1','2','3','4'):
        try:
            x=int(input("Enter a value"))
            y=int(input("Enter y value"))
        
    