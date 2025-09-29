n=int(input("enter a Number"))
sum_of_digit=0
while n>0:
    digit=n%10
    sum_of_digit+=digit
    n=n//10
print("Sum of digit",sum_of_digit)