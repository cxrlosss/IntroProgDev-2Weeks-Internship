def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def lcm(a, b):
    return (a * b) // gcd(a, b)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        print(a, b)
    return a

def calculator():
    result = 0
    while True:
        print("Current result: ", result)
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Greatest common divisor (gcd)")
        print("6. Least common multiple (lcm)")
        print("7. Continue with result")
        print("8. Stop")

        choice = input("Enter the number of the wished operation: ")

        if choice == '8':
            break

        if choice == '7':
            if result == 0:
                print("There is no result.")
                continue

            num2 = float(input("Enter the number you want to continue with: "))
            new_choice = input("Choose an operation: \n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Gcd\6. Lcm\.")

            if new_choice == '1':
                result = add(result, num2)
            elif new_choice == '2':
                result = subtract(result, num2)
            elif new_choice == '3':
                result = multiply(result, num2)
            elif new_choice == '4':
                result = divide(result, num2)
            elif new_choice == '5':
                result = gcd(result, num2)
            elif new_choice == '6':
                result = lcm(result, num2)
                                   
             
            else:
                print("Not possible. Choose a number you want to continue with.")

        else:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = gcd(result, num2)
            elif choice == '6':
                result = lcm(result, num2)
            
            else:
                print("Not possible. Choose a number from 1 to 6.")

        print("Result: ", result)
        print("-------------------------")

if __name__ == "__main__":
    calculator()

