def withdraw(accounts, amount,acc_name):
    accounts[acc_name]-= amount
    print(f"Withdrew ${amount}")