num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
print("1.Addition 2.Subtraction 3. Multiplication 4.Division")
choice=int(input("Enter a choice :"))

match choice:
    case 1:
        print("Addition :",num1+num2)
    case 2:
        print("Subtraction :",num1-num2)
    case 3:
        print("Multiplication :",num1*num2)
    case 4:
        print("Division:",num1/num2)