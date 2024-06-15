from transaction import Transaction
import csv

filepath = r"userdata/transaction_history.csv"

def csv_to_list() -> list:
    with open(filepath) as transactions:
        transactions_data = csv.reader(transactions)
    
        transactions_list = []
        for row in transactions_data:
            transactions_list.append(row)

        return transactions_list

def __get_latest_transaction_number() -> int:
    
    with open(filepath) as transactions:
        transactions_data = csv.reader(transactions)
    
        count = 0
        for row in transactions_data:
            count += 1

        return count - 1

def insert_transaction(new_transaction: Transaction):
    num = __get_latest_transaction_number()+1

    with open(filepath, "w", newline="") as transactions:
        writer = csv.writer(transactions)
        writer.writerow([num,new_transaction.date.isoformat(),new_transaction.amount,new_transaction.type_,new_transaction.category,new_transaction.comment])

def transaction_to_list(transaction: Transaction) -> list:
    transaction_list = [transaction.date.isoformat(),transaction.amount,transaction.type_,transaction.category,transaction.comment]
    return transaction_list

def list_to_transaction(transaction_list: list) -> Transaction:
    transaction = Transaction(transaction_list[0],transaction_list[1],transaction_list[2],transaction_list[3],transaction_list[4],transaction_list[5])
    return transaction