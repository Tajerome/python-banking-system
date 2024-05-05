# Question: Make a package called banking that contains the following functions:
# 1. deposit
# 2. withdraw
# 3. check_balance
# 4. create_account
# 5. delete_account
# 6. transfer

# # create_account will ask the use for the following information:
# the number of accounts to create
# the name of each account 
# the starting balance for each account

# Make a main file that imports the package and uses the functions to perform the following tasks:
# 1. Deposit $1000
# 2. Withdraw $500
# 3. Chec
# 3. Check balance
# 4. Transfer $100 to another account

def deposit(accounts, amount,acc_name):
    accounts[acc_name]+= amount
    print(f"Deposited ${amount}")
    

