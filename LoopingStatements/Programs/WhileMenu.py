while True:
    print("1. Say Hello\n2. Say Bye\n3. Exit")
    choice = int(input("Enter a Choice: "))
    if choice==1:
        print("Hello")
    elif choice==2:
        print("Bye")
    elif choice==3:
        print("Ok Exiting..")
        break
    else:
        print("Invalid Choice!")