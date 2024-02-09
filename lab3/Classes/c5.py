class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")


account_owner = input("The account owner's name: ")
initial_balance = float(input("The initial balance: "))

account = Account(owner=account_owner, balance=initial_balance)


deposit_amount = float(input("The amount to deposit: "))
account.deposit(deposit_amount)


withdraw_amount = float(input("The amount to withdraw: "))
account.withdraw(withdraw_amount)

