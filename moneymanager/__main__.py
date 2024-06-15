import display


def main() -> None:
    display.display_welcome()

    while True:
        option = display.prompt_main()
        match option:
            case 1:  # input expense
                display.prompt_input_expense()
            case 2:  # input income
                display.prompt_input_income()
            case 3:  # view balance
                display.prompt_view_balance()
            case 4:  # expense statistics
                display.prompt_expense_statistics()
            case 5:  # income statistics
                display.prompt_income_statistics()
            case _:
                print("Invalid input.")


if __name__ == "__main__":
    main()
