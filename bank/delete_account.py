# def delete_acc(accounts, name_acc):
#     for j in accounts:
#         if j['name'] == name_acc:
#             accounts.pop(j)
#             return j 

def delete_acc(accounts, name_acc):
    if name_acc in accounts:
        accounts.pop(name_acc)
        print(f"Account {name_acc} was deleted")
    else:
        print(f"Account {name_acc} was not found")