import csv
from datetime import datetime
import os
from unittest import TestCase

from moneymanager import csv_manager, transaction


class TestCsvManager(TestCase):

    # override
    def setUp(self) -> None:
        csv_manager.transaction_history_path = "temp_transaction_history.csv"
        with open(csv_manager.transaction_history_path, 'w') as file:
            file.write("no,date,account,amount,type,category,comment")

        self.__dummy_transaction = transaction.Transaction(
            datetime.now(),
            "mandiri",
            10000.50,
            "expense",
            "food",
            "ayam super"
        )
        self.__add_dummy_row(self.__dummy_transaction)

    def test_csv_to_list_returns_correct_lists(self) -> None:
        # ACT
        transaction_list = csv_manager.csv_to_list()
        # ASSERT
        self.assertEqual(transaction_list[0], 1)
        self.assertEqual(transaction_list[1], self.__dummy_transaction.date.isoformat())
        self.assertEqual(transaction_list[2], self.__dummy_transaction.account)
        self.assertEqual(transaction_list[3], self.__dummy_transaction.amount)
        self.assertEqual(transaction_list[4], self.__dummy_transaction.type_)
        self.assertEqual(transaction_list[5], self.__dummy_transaction.category)
        self.assertEqual(transaction_list[6], self.__dummy_transaction.comment)

    def __add_dummy_row(self, transaction: transaction.Transaction):
        with open(csv_manager.transaction_history_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow([
                1,
                transaction.date.isoformat(),
                transaction.account,
                transaction.amount,
                transaction.type_,
                transaction.category,
                transaction.comment
            ])

    # override
    def tearDown(self) -> None:
        os.remove(csv_manager.transaction_history_path)
