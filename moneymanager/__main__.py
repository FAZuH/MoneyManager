import display
import csv_manager


# def _do_input_expense():
#     expense = display.input_transaction("expense")
#     csv_manager.insert_transaction(expense)

# def _do_input_income():
#     income = display.input_transaction("income")
#     csv_manager.insert_transaction(income)

def add_transaction():
    _type = display.must_get_input(
        "Input expense or income?"
        "1. Expense"
        "2. Income", int
        )
    match _type:
        case 1: # Input expense
            new_transaction = display.input_transaction("expense")
            csv_manager.insert_transaction(new_transaction)
        case 2: # Input income
            new_transaction = display.input_transaction("income")
            csv_manager.insert_transaction(new_transaction)

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
            case 1:  # Add transaction
                add_transaction()
            case 2:  # Transaction history
                display.show_transaction_history()
            case 3:  # Account
                _do_view_balance()
            case 4:  # Statistics
                _do_expense_statistics()
            case _:
                print("Invalid input.")


if __name__ == "__main__":
    main()
