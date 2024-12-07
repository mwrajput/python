"""

Bank Account Simulation
Attributes: Account number, account holder, balance.

Methods:
Deposit: Add an amount to the balance.
Withdraw: Subtract an amount if the balance is sufficient.

Display Balance: Show the current balance.

Objective: 
Learn data validation and 
interaction between attributes and methods.

"""


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder  = account_holder
        self.balance = balance
    
    def deposit(self,amount):
        if amount > 0 :
            self.balance =  self.balance + amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else :
            print("You are entering a negative number. Deposit failed.")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance =  self.balance - amount 
        elif self.balance == 0:
            print("Insuficent Balance")
        else:
            print("Amount Must be Positive")            
            

    def get_balance(self):
        return f"Balance : {self.balance}"
    
    def account_details(self):
        return f"Hey!{self.account_holder}\nAccount No : {self.account_number}\nYour Balance is {self.balance} "
    

# Object Creation 

accountNo = 5252
name = "Muhammad Waqas"
balance = -6


Acc1 = BankAccount(accountNo, name, balance)

# amount = int(input("Enter amount : "))
Acc1.deposit(200)
# Acc1.withdraw(200)
# print(f" Widthdraw :\n\n{Acc1.account_details()}\n\n")






        