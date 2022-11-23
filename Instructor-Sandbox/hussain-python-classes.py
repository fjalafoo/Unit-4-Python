class BankAccount():
    def __init__(self):
        self.balance = 4800
    def check_balance(self):
        print(f'your balance is {self.balance}')
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
        print(f'your balance is {self.balance}')
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
            print(f'your balance is {self.balance}')
        else:
            print("\n Insufficient balance  ")
    def accumulate_interest(self):
        self.interest = 0.02
        self.balance = self.balance + (self.interest*self.balance)
    def display(self):
        print("\n Net Available Balance=",self.balance)

s = BankAccount()
s.check_balance()
s.deposit()
s.withdraw()
# s.accumulate_interest()
s.display()