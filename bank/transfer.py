def transfer(accounts,sender,receiver,amount):
    accounts[sender]-=amount
    accounts[receiver]+= amount
    print(f"Transferred ${amount} from {sender} to {receiver}")
