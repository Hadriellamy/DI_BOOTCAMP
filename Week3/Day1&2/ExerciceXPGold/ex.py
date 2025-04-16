
#Exercise 1: Bank Account
"""
Instructions

Part I:

Create a class called BankAccount that contains the following attributes and methods:
balance - (an attribute)
__init__ : initialize the attribute
deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive


Part II : Minimum balance account

Create a MinimumBalanceAccount that inherits from BankAccount.
Extend the __init__ method and accept a parameter called minimum_balance with a default value of 0.
Override the withdraw method so it only allows the user to withdraw money if the balance remains higher than the minimum_balance, raise an Exception if not.


Part III: Expand the bank account class

Add the following attributes to the BankAccount class:
username
password
authenticated (False by default)

Create a method called authenticate. This method should accept 2 strings : a username and a password. If the username and password match the attributes username and password the method should set the authenticated boolean to True.

Edit withdraw and deposit to only work if authenticated is set to True, if someone tries an action without being authenticated raise an Exception


Part IV: BONUS Create an ATM class

__init__:
Accepts the following parameters: account_list and try_limit.

Validates that account_list contains a list of BankAccount or MinimumBalanceAccount instances.
Hint: isinstance()

Validates that try_limit is a positive number, if you get an invalid input raise an Exception, then move along and set try_limit to 2.
Hint: Check out this tutorial

Sets attribute current_tries = 0

Call the method show_main_menu (see below)

Methods:
show_main_menu:
This method will start a while loop to display a menu letting a user select:
Log in : Will ask for the users username and password and call the log_in method with the username and password (see below).
Exit.

log_in:
Accepts a username and a password.

Checks the username and the password against all accounts in account_list.
If there is a match (ie. use the authenticate method), call the method show_account_menu.
If there is no match with any existing accounts, increment the current tries by 1. Continue asking the user for a username and a password, until the limit is reached (ie. try_limit attribute). Once reached display a message saying they reached max tries and shutdown the program.

show_account_menu:
Accepts an instance of BankAccount or MinimumBalanceAccount.
The method will start a loop giving the user the option to deposit, withdraw or exit.

"""

#Part 1 BankAccount simple

class BankAccount:
    def __init__(self, username, password):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise Exception("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}")

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print(f"Authenticated successfully as {self.username}")
            return True
        return False


#Part 2 MinimumBalanceAccount

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw beyond minimum balance.")
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}")


#Part 3&4 ATM class

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise Exception("All accounts must be instances of BankAccount or its subclasses.")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit. Defaulting to 2.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                self.show_account_menu(account)
                return

        self.current_tries += 1
        print("Login failed.")
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu for {account.username} ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter choice: ")

            try:
                if choice == "1":
                    amount = int(input("Amount to deposit: "))
                    account.deposit(amount)
                elif choice == "2":
                    amount = int(input("Amount to withdraw: "))
                    account.withdraw(amount)
                elif choice == "3":
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice.")
            except Exception as e:
                print("Error:", e)



#Exemple 

if __name__ == "__main__":
    account1 = BankAccount("john", "1234")
    account2 = MinimumBalanceAccount("jane", "abcd", minimum_balance=100)

    atm = ATM([account1, account2])


