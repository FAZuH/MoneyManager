import csv

from transaction import Transaction


transaction_history_path = "userdata/transaction_history.csv"


def csv_to_list() -> list:
    with open(transaction_history_path) as transactions:
        transactions_data = csv.reader(transactions)
    
        transactions_list = []
        for row in transactions_data:
            transactions_list.append(row)

        return transactions_list

def _get_latest_transaction_number() -> int:
    with open(transaction_history_path) as transactions:
        transactions_data = csv.reader(transactions)
        
        count = 0
        for row in transactions_data:
            count += 1

        return count - 1

def transaction_to_list(transaction: Transaction) -> list:
    transaction_list = [transaction.date.isoformat(),transaction.amount,transaction.type_,transaction.category,transaction.comment]
    return transaction_list

def list_to_transaction(transaction_list: list) -> Transaction:
    transaction = Transaction(transaction_list[0],transaction_list[1],transaction_list[2],transaction_list[3],transaction_list[4],transaction_list[5])
    return transaction

def insert_transaction(new_transaction: Transaction):
    with open(transaction_history_path, "w", newline="") as transactions:
        writer = csv.writer(transactions)

        num = _get_latest_transaction_number()+1
        new_row = [num, *new_transaction]

        writer.writerow(new_row)
