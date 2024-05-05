from bank.deposit import deposit
from bank.withdraw import withdraw
from bank.check_balance import check_balance
from bank.create_account import create_account
from bank.delete_account import delete_acc
from bank.transfer import transfer

accounts={}

def main():
    while True:
        # menu options
        print("Would you like to:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Create Account")
        print("5. Delete Account")
        print("6. Transfer")
        print("7. Exit")
        choice = input("Enter your choice: ") 
        if choice == "1":
            acc_name = input("Which account would you like to deposit $ into: ")
            amount = int(input("Enter amount: $"))
            if acc_name in accounts:
                deposit(accounts,amount,acc_name)
                print(accounts[acc_name])
            # deposit(accounts[num_acc - 1], amount)
            else:
                print("Account not found")
        
        if choice == "2":
            acc_name = input("Which account do you want to withdraw $ from: ")
            amount = int(input("Enter amount: $"))
            if acc_name in accounts:
                withdraw(accounts,amount,acc_name)
            else:
                print("Account not found")
        
        elif choice == "3":
            acc_name = input("Check balance for which account?: ")
            if acc_name in accounts:
                check_balance(accounts,acc_name)
            else:
                print("Account not found")
        
        elif choice == "4":
            acc_name = input("Enter a name for your account: ")
            initial_amount = float(input("Enter initial amount: $"))
            create_account(accounts,acc_name,initial_amount)

        elif choice == "5":
            acc_name = input("Which account would you like to delete: ")
            delete_acc(accounts, acc_name)
        
        elif choice == "6":
            sender = input("Enter sender name: ")
            receiver = input("Enter receiver name: ")
            amount = int(input("Enter amount to transfer: $"))
            if sender in accounts and receiver in accounts:
                transfer(accounts,sender,receiver,amount)
            else:
                print("Invalid Account")
        elif choice == "7":
            print("Exiting program")
            break
        # else:
        #     print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()