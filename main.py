def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    num1 = int(input("Enter The First Number  : "))
    num2 = int(input("Enter The Second Number : "))
    print("(",end=" ")
    print("+",end=",  ")
    print("-",end=",  ")
    print("*",end=",  ")
    print("/",end=",  ")
    print(")",end="")

    select = input("Select Choice for operation : ")

    if select == "+":
        print(add(num1, num2))
    elif select == "-":
        print(sub(num1, num2))
    elif select == "*":
        print(multiply(num1, num2))
    elif select == "/":
        print(divide(num1, num2))
    else:
        print("Invalid Choice")

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break