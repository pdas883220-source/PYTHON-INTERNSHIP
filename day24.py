class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount.")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Account Balance:", self.__balance)


account = BankAccount("Purnima", 1000)

account.display_balance()

account.deposit(500)

account.display_balance()

