from moneymanager.database.base_csv_repository import BaseCsvRepository
from moneymanager.database.model.account import Account
from moneymanager.database.repository.repository import Repository


class AccountRepository(BaseCsvRepository, Repository[Account, str]):
    def select(self, identifier: str) -> Account:
        # try:
        with self.enter_reader() as reader:
            rows = list(reader)
            for i in range(len(rows)):
                if rows[i]["name"] == identifier:
                    return self.model(rows[i]["name"], float(rows[i]["balance"]))
        # If account with name identifier not found
        raise ValueError(f"Account with name {identifier} not found")

    def insert(self, entity: Account) -> None:  # Method for inserting a new account
        with self.enter_reader() as reader:
            rows = list(reader)  # Turns into a list
            for i in range(len(rows)):
                if rows[i]["name"] == entity.name:  # If account name is already exist
                    raise ValueError(f"Account with name {entity.name} is already exist!")
        # If the account hasn't been created
        with self.enter_writer() as writer:
            writer.writerow({"name": entity.name, "balance": entity.balance})

    def update(self, identifier: str, entity: Account) -> None:
        available = False
        with self.enter_reader() as reader:
            rows = list(reader)
            print(rows)
            for i in range(len(rows)):
                if rows[i]["name"] == identifier:  # If found
                    available = True
                    rows[i]["name"] = entity.name  # Overwrite the new name to the row list
                    rows[i]["balance"] = entity.balance  # Overwrite the new balance to the row list
            # print(rows)

        if available:
            with self.enter_writer(mode="w") as writer:
                writer.writeheader()
                writer.writerows(rows)
                return
        else:
            # If the account doesn't exist
            raise ValueError(f"Account with name {identifier} is not exist!")

    def delete(self, identifier: str) -> None:
        available = False
        with self.enter_reader() as reader:
            rows = list(reader)
            with self.enter_writer("w") as writer:
                for i in range(len(rows)):
                    if rows[i]["name"] != identifier:  # If found
                        writer.writerow({"name": rows[i]["name"], "balance": rows[i]["balance"]})
                    else:
                        available = True

        if available:
            return
        else:  # If the account doesn't exists
            raise ValueError(f"Account with name {identifier} is not exist!")

    def select_all(self) -> list[Account]:
        with self.enter_reader() as reader:
            return [self.model(**row) for row in reader]  # type: ignore

    @property
    def filename(self) -> str:
        return "accounts.csv"

    @property
    def model(self) -> type[Account]:
        return Account
