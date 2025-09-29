n = int(input("Enter a number: "))

while n > 9:  
    sum_of_digit = 0
      
    while n > 0:
        digit = n % 10
        sum_of_digit += digit
        n //= 10
    n = sum_of_digit

print("Final single-digit sum:", n)
