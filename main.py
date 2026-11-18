import json

def loadtransaction():
    with open('transactions.json','r')as file:
        data = json.load(file)
    return data

def savetransaction():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file,indent=4)

transactions = loadtransaction()

def addtransaction():
    num_tr = int(input("Number of transactions to add: "))
    for i in range(num_tr):
        tr_type = input("Transaction Type(Income or Expense): ")
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Enter a valid amount..!")
            continue
        category = input("Category: ")
        description = input("Description: ")
        date = input("Date: ")
        transaction = {
            "id": max([transaction["id"] for transaction in transactions], default=0) + 1,
            "type": tr_type,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        transactions.append(transaction)
        savetransaction()
def viewtransaction():
    v_id = int(input("Enter your transaction ID: "))
    for transaction in transactions:
        if transaction["id"] == v_id:
            print(f"Transaction ID:{transaction['id']}\n Type:{transaction['type']}\n Amount:{transaction['amount']}\n Category:{transaction['category']}\n Date:{transaction['date']}")
            break
def deletetransaction():
        del_id = int(input("Enter your transaction ID: "))

        found_transaction = None

        for transaction in transactions:
            if transaction["id"] == del_id:
                found_transaction = transaction
                break

        if found_transaction is None:
            print("Transaction ID does not exist!")
        else:
            transactions.remove(found_transaction)
            savetransaction()
            print("Transaction deleted successfully!")

def view_analysis():
    total_income = 0
    total_expense = 0
    for transaction in transactions:
        if transaction["type"].lower() == "income":
            total_income += transaction["amount"]
        elif transaction["type"].lower() == "expense":
            total_expense += transaction["amount"]
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance:{total_income - total_expense}")



while True:
    print("----CLI-Expense Tracker----\n")
    print("1. Add Transaction")
    print("2. View Transactions ")
    print("3. Delete Transaction")
    print("4. Analysis")
    print("5. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        addtransaction()
    elif option == 2:
        if len(transactions) < 1:
            print("No transactions found..!")
        else:
            viewtransaction()
    elif option == 3:
        deletetransaction()
    elif option == 4:
        view_analysis()
    elif option == 5:
        print("Have a Nice Day \n Exiting..")
        break
    else:
        print("Invalid Option")

