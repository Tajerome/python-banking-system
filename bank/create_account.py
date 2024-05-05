# # create_account will ask the use for the following information:
# the number of accounts to create
# the name of each account 
# the starting balance for each account

def create_account(accounts,acc_name,initial_amount):
    accounts[acc_name]=initial_amount
    print(f"Account {acc_name} created with ${initial_amount}")