def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
a = int(input("Enter"))
b = int(input("Enter"))
result = gcd(a, b)
print(f"GCD of {a} and {b} is {result}")
