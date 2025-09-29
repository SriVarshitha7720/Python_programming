def find_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

n = int(input("Enter a number: "))
print("Factors of", n, "are:")
find_factors(n)
