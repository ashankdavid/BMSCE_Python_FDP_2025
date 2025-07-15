acct_balance = int(input("Enter your Account Balance: "))
amount = int(input("How much you want to withdraw?: "))

if amount > 0:
    if amount <= acct_balance:
        print("Transaction Successfull")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Amount!")