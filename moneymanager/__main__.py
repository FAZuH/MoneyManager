import display
import csv_manager


def _do_input_expense():
    expense = display.input_transaction("expense")
    csv_manager.insert_transaction(expense)

def _do_input_income():
    income = display.input_transaction("income")
    csv_manager.insert_transaction(income)

def _do_view_balance():
    return

def _do_expense_statistics():
    return

def _do_income_statistics():
    return


def main() -> None:
    display.display_welcome()

    while True:
        option = display.input_main()
        match option:
            case 1:  # input expense
                _do_input_income()
            case 2:  # input income
                _do_input_expense()
            case 3:  # view balance
                _do_view_balance()
            case 4:  # expense statistics
                _do_expense_statistics()
            case 5:  # income statistics
                _do_income_statistics()
            case _:
                print("Invalid input.")


if __name__ == "__main__":
    main()
