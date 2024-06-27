import csv
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from moneymanager.transaction import Transaction


class TransactionModel:

    TRANSACTION_HISTORY_PATH = "userdata/transaction_history.csv"

    def add_transaction(self, transaction: Transaction) -> None:
        num = self.__get_latest_transaction_number() + 1
        new_transaction_list = transaction.to_list()
        new_row = [num, *new_transaction_list]

        with open(self.TRANSACTION_HISTORY_PATH, "a", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(new_row)

    def edit_transaction(self) -> None:
        pass

    def remove_transaction(self) -> None:
        pass

    def show_transaction(self) -> None:
        pass

    def __read_transaction_history(self) -> list[list[str]]:
        with open(self.TRANSACTION_HISTORY_PATH) as stream:
            transactions_data = csv.reader(stream)

            transactions_list = list(transactions_data)
            return transactions_list

    def __get_latest_transaction_number(self) -> int:
        transactions = self.__read_transaction_history()

        latest_transaction = transactions[-1]
        latest_transaction_number = latest_transaction[0]

        if latest_transaction_number == "no":
            return 0

        return int(latest_transaction_number)
