transactions = []
def addtransaction():
    num_tr = int(input("Number of transactions to add: "))
    for i in range(num_tr):
        tr_type = input("Transaction Type(Income or Expense): ")
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Enter a valid amount..!")
            exit()
        category = input("Category: ")
        description = input("Description: ")
        date = input("Date: ")
        transaction = {
            "id": len(transactions) + 1,
            "type": tr_type,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        transactions.append(transaction)

while True:
    print("----CLI-Expense Tracker----\n")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit\n")
    option = int(input("Enter your option: "))
    if option == 1:
        addtransaction()
    elif option == 2:
        if len(transactions) < 1:
            print("No transactions found..!")
        else:
            print("----Transactions---\n")
            for i in transactions:
                print(f"Transaction id: {i['id']}\nTransaction Type: {i['type']},\nAmount: {i['amount']}\nCategory:{i['category']},\nDescription:{i['description']}\n")
    elif option == 3:
        print("Have a Nice Day \n Exiting..")
        break
    else:
        print("Invalid Option")

