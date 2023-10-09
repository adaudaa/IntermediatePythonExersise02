from BankAccount import BankAccount
my_account = BankAccount("John's Account", 70.00)
my_account.deposit(29.00)
my_account.withdraw(10.00)
balance_message = my_account.get_balance()
print(balance_message)