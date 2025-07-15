def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))

    operation = int(input("Choose a Operation:\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit\n"))

    match operation:
        case 1:
            print("Your addition result is: ", add(num1, num2))
        case 2:
            print(sub(num1, num2))
        case 3:
            print(mul(num1, num2))
        case 4:
            print(div(num1, num2))
        case 5:
            print("OKAY BYEEE")
            break
        case _:
            print("Invalid Opeartion Entered")