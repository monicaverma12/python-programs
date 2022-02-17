class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def total_funds(self):
        funds = 0
        for customer in self.customers:
            funds = funds + customer.total_funds()
        return funds


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_funds(self):
        funds = 0
        for account in self.accounts:
            funds = funds + account.total_funds()
        return funds


class Account:
    def __init__(self, amount):
        self.amount = amount

    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount = self.amount - amount

    def deposit(self, amount):
        self.amount = self.amount + amount

    def total_funds(self):
        return self.amount


# Example usage of the three classes
pybank = Bank("Python Savings and Trust")

john = Customer("John Smith")
john_savings = Account(1842.15)
john_checking = Account(298.11)

john.add_account(john_savings)
john.add_account(john_checking)

pybank.add_customer(john)

# print("Total funds: %s" % pybank.total_funds())

username = input('Enter your name (Type "John Smith"): ')

while username != "John Smith":
    username = input('%s is not a customer at this Bank. Please try again: ' % username)

print("\n\nWelcome, %s. Please select from the following options:" % username)
print("\t1. Deposit money.")
print("\t2. Withdraw money.")
print("\t3. Transfer money between your checking and savings.")
print("\t4. Log out.")

option = input('Input an option: ')

available_options = ['1', '2', '3', '4']

while option not in available_options:
    option = input("Invalid option. Try again: ")

while option != '4':
    if option == '1':
        print("\n\nSelect the account into which you would like to deposit money: ")
        print("\t1. Checking account")
        print("\t2. Savings account")
        account = input("Input an option: ")
        account_options = ['1', '2']
        while account not in account_options:
            account = input("Invalid option. Try again: ")
        amount = input("Enter the amount to deposit: ")
        deposit = 0.0
        try:
            deposit = float(amount)
        except ValueError:
            print("Invalid input. No transaction was done.")
        if account == '1':
            john_checking.deposit(deposit)
        else:
            john_savings.deposit(deposit)
        print("Amount in checking: %s" % john_checking.total_funds())
        print("Amount in savings: %s" % john_savings.total_funds())
        print("Total funds: %s" % pybank.total_funds())
    elif option == '2':
        print("\n\nSelect the account from which you would like to withdraw money: ")
        print("\t1. Checking account")
        print("\t2. Savings account")
        account = input("Input an option: ")
        account_options = ['1', '2']
        while account not in account_options:
            account = input("Invalid option. Try again: ")
        amount = input("Enter the amount to withdraw: ")
        withdraw = 0.0
        try:
            withdraw = float(amount)
        except ValueError:
            print("Invalid input. No transaction was done.")
        if account == '1':
            john_checking.withdraw(withdraw)
        else:
            john_savings.withdraw(withdraw)
        print("Amount in checking: %s" % john_checking.total_funds())
        print("Amount in savings: %s" % john_savings.total_funds())
        print("Total funds: %s" % pybank.total_funds())
    else:
        print("\n\nSelect the transaction you would like to perform: ")
        print("\t1. Checkings to savings")
        print("\t2. Savings to checking")
        account = input("Input an option: ")
        account_options = ['1', '2']
        while account not in account_options:
            account = input("Invalid option. Try again: ")
        amount = input("Enter the amount to transfer: ")
        transfer = 0.0
        try:
            transfer = float(amount)
        except ValueError:
            print("Invalid input. No transaction was done.")
        if account == '1':
            john_checking.withdraw(transfer)
            john_savings.deposit(transfer)
        else:
            john_savings.withdraw(transfer)
            john_checking.deposit(transfer)
        print("Amount in checking: %s" % john_checking.total_funds())
        print("Amount in savings: %s" % john_savings.total_funds())
        print("Total funds: %s" % pybank.total_funds())

    print("\n\nPlease select from the following options:")
    print("\t1. Deposit money.")
    print("\t2. Withdraw money.")
    print("\t3. Transfer money between your checking and savings.")
    print("\t4. Log out.")
    option = input("Input an option: ")
    while option not in available_options:
        option = input("Invalid option. Try again: ")

print("\n\nThank you for your business. Have a nice day.")