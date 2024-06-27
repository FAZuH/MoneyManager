import display
from moneymanager.account_model import AccountModel
from moneymanager.transaction_model import TransactionModel


account_model = AccountModel()
transaction_model = TransactionModel()


def do_view_add_transaction():
    """
    Choose:
        1: Add expense
        2: Add income
        3: Back
    """
    option_mapping = {
        1: "expense",
        2: "income",
        3: "exit"
    }

    while True:
        option_int = display.choose_transaction_type()

        if option_int not in option_mapping:
            print("Invalid input")
            continue

        option = option_mapping[option_int]

        if option == "exit":
            display.clear_view()
            return

        transaction = display.input_transaction(option)  # type: ignore
        transaction_model.add_transaction(transaction) 


def do_view_transaction_history():
    """
    1. Show daily transaction history
    2. Choose: 
        1. daily
        2. weekly
        3. monthly
        4. yearly
        5. custom
        6. exit

    For each option, show expense and income (transaction type).
    For each transaction type, show total balance change for each transaction category.
    For each session, Choose: next, previous, history period.
        If there's no more transactions to show on option next/previous, don't show the option.
    """
    option = "daily"
    display.show_transaction_history(option)

    option_mapping = {
        1: "daily",
        2: "weekly",
        3: "monthly",
        4: "yearly",
        5: "custom",
        6: "exit",
    }

    while True:
        option_int = choose_history_period()

        if option_int not in option_mapping:
            print("Invalid input")
            continue

        option = option_mapping[option_int]

        if option == "exit":
            display.clear_view()
            return

        display.show_transaction_history(option)

def do_view_account():
    """
    1. Show existing account. name and their corresponding balance
    2. Choose: show, add, edit, remove, transfer, exit
        show: show all existing account: name and their corresponding balance
        add: adds a new account. Prompts: name, balance (initial)
        edit: edits existing account. Prompts: account_id (to edit), name (new), balance (new)
        remove: removes existing account. Prompts: account_id (to remove)
        transer: Transfer balance between existing accounts. Prompts: account_from, account_into, balance
    3. Show success message
    4. Go to step 1.
    """
    option_mapping = {
        1: "show",
        2: "add",
        3: "edit",
        4: "remove",
        5: "transfer",
        6: "exit"
    }

    while True:
        option_int = display.choose_account_type()
        option = option_mapping[option_int]

        match option:
            case "show":
                account_model.show_accounts()
            case "add":
                account = display.input_new_account()
                account_model.add_account(account)
            case "edit":
                id_to_edit, account = display.input_edit_account()
                account_model.edit_account(id_to_edit, account)
            case "remove":
                account_id = display.input_account_id()
                account_model.remove_account(account_id)
            case "transfer":
                account_id_from, account_id_into, balance = display.input_transfer_account()
                account_model.transfer_balance(account_id_from, account_id_into, balance)
            case "exit":
                display.clear_view()
                return
            case _:
                print("Invalid input")


def do_view_transaction_statistics():
    return


def main() -> None:
    display.show_welcome()

    while True:
        option = display.choose_main()
        display.clear_view()

        match option:
            case 1:  # Add transaction
                do_view_add_transaction()
            case 2:  # Transaction history
                do_view_transaction_history()
            case 3:  # Account
                do_view_account()
            case 4:  # Statistics
                do_view_transaction_statistics()


if __name__ == "__main__":
    main()
