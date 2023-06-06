

def calculator():
    result=0

while True:
    number1=float(input("1. number:"))
    number2=float(input("2. number:"))
    arethmetic_operator=input("add? (+), subtract? (-), multiply? (*), divide? (/):")

    if arethmetic_operator=="+" :
        result=number1+number2
    if arethmetic_operator=="-" :
        result=number1-number2
    if arethmetic_operator=="*" :
        result=number1*number2
    if arethmetic_operator=="/" :
        result=number1/number2


    print("The current result is:", result)
    print("Choose an operation:")
    print("1. Continue")
    print("2. Stop")

    option = input("Enter the wished operation:")
    if option == "2":
        break

