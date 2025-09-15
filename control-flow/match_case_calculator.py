num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sign = input("Choose the operation (+, -, *, /): ")

    
match sign:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        result = num1 / num2
    case '*':
        result = num1 * num2

print("The result is", result)