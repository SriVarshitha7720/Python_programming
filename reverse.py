def reverse(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


n = int(input("Enter a number: "))
print("Reversed number:", reverse(n))
