class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(self.owner, "'s current:", self.balance)

    def withdraw(self, money):
        if money > self.balance:
            print("Your balance will be overdrawn!")
        else:
            self.balance -= money
            print(self.owner, "'s current balance:", self.balance)

class Account(Bank):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

print("Enter acc1 data: ")
acc1 = Account(input(), int(input()))
print("Enter acc2 data: ")
acc2 = Account(input(), int(input()))

print("Enter acc1 deposit and withdraw: ")
acc1.deposit(int(input()))
acc1.withdraw(int(input()))
print("Enter acc2 deposit and withdraw: ")
acc2.deposit(int(input()))
acc2.withdraw(int(input()))