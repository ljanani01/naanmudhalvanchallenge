#Implement a class called Bank Account that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.
class BankAccount:
 def __init__(self,account_number,account_holder_name,initial_balance=0.0):
  self.__account_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance = initial_balance

 def deposit(self, amount):
  if amount > 0:
   self.__account_balance += amount
   return (f"Deposited ${amount}.New balance:${self.__account_balance}")
  else:
   return ("Invalid deposit amount. Amount must be greater than 0")

 def withdraw(self, amount):
  if amount > 0 and amount <=  self.__account_balance:
   self.__account_balance -= amount
   return (f"Withdrew ${amount}.New balance:${self.__account_balance}")
  else:
   return ("Invalid withdrawal amount or insufficient balance")

 def display_balance(self):
  return (f"Account Balance for {self.__account_holder_name}:${self.__account_balance}")
# Creating an instance of BankAccount
account = BankAccount("1234567890", "John Doe", 1000.0)
# Testing deposite and withdrawal functionality
print(account.display_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500))
#This should result in an error message