
# class BankAccount():
#     def __init__(self, type, balance = 0, overdraft_fees = 0):
#         self.type = type
#         self.balance = balance
#         self.overdraft_fees = overdraft_fees

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         # if our balance becomes negative, prevent withdrawing money
#         current_balance = self.balance - amount
#         if ((current_balance - self.overdraft_fees) < -100):
#             print("You cannot withdraw money, insufficient funds")
#             return 0

#         if (current_balance > 0):
#             self.balance -= amount
#             return amount
#             # return self.balance
#         else: # negative current_balance
#             self.overdraft_fees += 20
#             self.balance -= amount
#             return amount


#     def __str__(self):
#         return f"Your {self.type} account balance is: {self.balance} and your overdraft fees are: {self.overdraft_fees}"

# my_savings = BankAccount('savings', 50)

# my_checking = BankAccount('checking')

# money = my_savings.withdraw(100)
# print(my_savings)
# money = my_savings.withdraw(100)
# print(my_savings)

# my_checking.deposit(money)
# print(my_checking)



class BankAccount():
    def __init__(self,balance, interest = 0.02):
        self.balance = balance
        self.interest = interest

    def check_balance(self):
        return f"Your balance is: {self.balance}"
    
    def deposit(self, amount):
        if (amount <= 0):
            return False #boolean value
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if (amount <= 0):
            return False
        else:
            self.balance -= amount
            return self.balance

    def accumulate_interest(self):
        self.balance = self.balance * (self.interest + 1)
        # self.balance =+ self.balance * self.interest
        # self.balance = self.balance + (self.interest*self.balance)
        return self.balance


class ChildrensAccount(BankAccount):
    def __init__(self, balance, interest = 0):
        BankAccount.__init__(self, balance, interest)
        # super()
    
    def accumulate_interest(self):
        self.balance += 10



class OverDraftAccount(BankAccount):
    def __init__(self, balance, interest, overdraft_penalty = 40):
        BankAccount.__init__(self,balance,interest)
        self.overdraft_penalty = overdraft_penalty

    def withdraw(self, amount):
        current_balance = self.balance - amount
        if current_balance < 0:
            self.balance -= self.overdraft_penalty
            return False
        else:
            self.balance -= amount
            return self.balance

    def accumulate_interest(self):
        if self.balance <= 0:
            return 
        else: 
            self.balance = self.balance * (self.interest + 1)
            return self.balance

