class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self._balance = balance # Protected
        self.__pin = pin # Private

    def showBalance(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance is: {self._balance}")
        print(f"PIN: {self.__pin}")

acc = BankAccount("Ashank", 10000, 1234)

print(acc.name)
print(acc._balance) #
# print(acc.__pin)
acc.showBalance()
